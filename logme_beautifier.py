import sys

def usage(fname):
    print(f'python3 {fname} <text_file_to_beautify>')
    print(f'Example: python3 {fname} my_log_file.txt')
    exit(-1)
    
if len(sys.argv) != 2:
    usage(sys.argv[0])
else:
    filename = sys.argv[1]

map = {
        'Key.ctrl': '[CTRL]',
        'Key.shift': '[SHIFT]',
        'Key.shift_r': '[SHIFT]',
        'Key.space': ' ',
        'Key.tab': '\t',
        'Key.enter': '\n',
        'Key.cmd': '[CMD]',
        'Key.alt': '[ALT]',
        'Key.esc': '[ESC]',
        'Key.page_up': '[PG_UP]',
        'Key.page_down': '[PG_DOWN]',
        'Key.up': '[UP]',
        'Key.down': '[DOWN]',
        'Key.right': '[RIGHT]',
        'Key.left': '[LEFT]'
        # Add Other keys here
        }

# Store every line as list
with open(filename) as f:
    lines_list = f.readlines()

# This will hold beautified data, but in list form
data = []
data_with_backspace = []
for line_raw in lines_list:
    # The key that was pressed
    key = line_raw.strip().split()[2]
    
    # if backspace was pressed, instead of writing [BACKSPACE],
    # delete the last character from the list
    if data:
        if key == 'Key.backspace':
            data.pop()
            data_with_backspace.append('[BACK]')
            continue

    if key in map.keys():
        data.append(map[key])
        data_with_backspace.append(map[key])
    else:
        # Get only the character that is between single quotations
        data.append(key[1])
        data_with_backspace.append(key[1])


# If the same key was pressed multiple times,
# instead of printing every key,
# print the key that was pressed followed by the number of times it was pressed
# Ex: [ALT][ALT][ALT] will get converted into [ALT]<3>
# But aaa will NOT get converted into a[3]

j = 0
for item in data:
    if item not in map.values():
        j+=1
        continue
    c = 0
    for item_plus in data[j+1:len(data)]:
        if item_plus == item:
            c+=1
        else:
            if c != 0:
                for i in range(c+1):
                    data.pop(j)
                data.insert(j, f'{item}<{c+1}>')
            c=0
            break
    j+=1

with open('good.txt', 'w') as fd:
    fd.write(''.join(data))
    fd.write('\n'*5 + '='*40 + '\nNot so beautified data\n' + '='*40 + '\n\n')
    fd.write(''.join(data_with_backspace))
