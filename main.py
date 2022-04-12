# command = 'join file_path file_path column_name join_type'


def join_inner(f1, f2, index1, index2, headers1, headers2):
    for line1 in f1:
        line1 = line1.strip().split(',')
        for line2 in f2:
            line2 = line2.strip().split(',')
            if line1[index1] == line2[index2]:
                # TODO: print all values from both files, even if they are the same
                print(','.join([line1[i] for i in range(len(headers1))] + [line2[i] for i in range(len(headers2)) if headers2[i] not in headers1]))
        f2.seek(0)


def join_left(f1, f2, index1, index2, headers1, headers2):
    for line1 in f1:
        line1 = line1.strip().split(',')
        bool_found = False
        for line2 in f2:
            line2 = line2.strip().split(',')
            if line1[index1] == line2[index2]:
                print(','.join([line1[i] for i in range(len(headers1))] + [line2[i] for i in range(len(headers2)) if headers2[i] not in headers1]))
                bool_found = True
        if not bool_found:
            print(','.join([line1[i] for i in range(len(headers1))] + ['' for i in range(len(headers2)) if headers2[i] not in headers1]))
        f2.seek(0)


def main(*args):
    if len(args) != 4:
        print('Not enough arguments')
        return
    file_path1 = args[0]
    file_path2 = args[1]
    column_name = args[2]
    join_type = args[3]
    if join_type not in ['inner', 'left', 'right']:
        print('Invalid join type')
        return
    if not file_path1.endswith('.csv') or not file_path2.endswith('.csv'):
        print('Invalid file extension')
        return
    try:
        with open(file_path1, 'r') as f1, open(file_path2, 'r') as f2:
            header1 = f1.readline().strip().split(',')
            header2 = f2.readline().strip().split(',')
            if column_name not in header1 or column_name not in header2:
                print('Invalid column name')
                return
            index1 = header1.index(column_name)
            index2 = header2.index(column_name)

            if join_type == 'inner':
                print(','.join([i + '_1' for i in header1] + [i + '_2' for i in header2 if i not in header1]))
                join_inner(f1, f2, index1, index2, headers1=header1, headers2=header2)
            elif join_type == 'left':
                print(','.join([i + '_1' for i in header1] + [i + '_2' for i in header2 if i not in header1]))
                join_left(f1, f2, index1, index2, headers1=header1, headers2=header2)
            elif join_type == 'right':
                print(','.join([i + '_2' for i in header2] + [i + '_1' for i in header1 if i not in header2]))
                join_left(f2, f1, index2, index1, headers1=header2, headers2=header1)
    except FileNotFoundError:
        print('File not found')


if __name__ == '__main__':
    main('data/file1.csv', 'data/file2.csv', 'id', 'right')
