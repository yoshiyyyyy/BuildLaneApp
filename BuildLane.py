import openpyxl
import random

def func(filename,excel_row):

    wb = openpyxl.load_workbook('./static/uploads/%s' % filename)
    sheet1 = wb['Sheet1']
    sheet2 = wb['Sheet2']
    lane = {'A':1,'B':2,'C':3,'D':4,'E':5,'F':6,'G':7,'H':8}


    def get_value_list(t_2d):
        return([[cell.value for cell in row] for row in t_2d])


    def set_8values_lists(l_2d,num):
        for _  in range(num):
            l_3d = []
            for j in random.sample(l_2d, 8):
                l_3d.append(j)
                del l_2d[l_2d.index(j)]
            l_1d.append(l_3d)
    

    def set_7values_lists(l_2d,num2):
        for _ in range(num2):
            l_4d = []
            for k in random.sample(l_2d, 7):
                l_4d.append(k)
                del l_2d[l_2d.index(k)]
            l_1d.append(l_4d)

        

    def write_lists(sheet2, l_1d, start_row, start_col):
        r = 1
        for row1 in l_1d:
            r += 1
            c = 0
            row3 = sorted(row1,key=lambda x: x[1])
            for row2 in row3:
                new_cell = ','.join(map(str,row2))
                sheet2.cell(row=start_row + r,column=start_col + c ,value=new_cell)
                c += 1
                
                
    def remake_format(num_of_cell):
        for _  in range(num_of_cell):
            sheet2.insert_cols(1)
        sheet2.move_range("O2:O80", cols=-14)
        sheet2.move_range("M2:M80", cols=-11) 
        sheet2.move_range("K2:K80", cols=-8)
        sheet2.move_range("I2:I80", cols=-5) 
        sheet2.move_range("J2:J80", cols=-5) 
        sheet2.move_range("L2:L80", cols=-6) 
        sheet2.move_range("N2:N80", cols=-7) 
        sheet2.move_range("P2:P80", cols=-8) 
        for m,n in lane.items():
            sheet2['{}1'.format(m)] = '第{}レーン'.format(n)
            
            
            


    l_1d = []
    #-------------------------------------------------------------------------------------
    # 以下の"B255"の箇所はサンプルに合わせてあります。
    # NewLaneのSheet1で対象となるデータのカラムの範囲に合わせて適宜変更してください。
    #-------------------------------------------------------------------------------------
    l_2d = get_value_list(sheet1['A2:B%d' % excel_row])
    

    if len(l_2d) % 8 == 0:
        num = len(l_2d) // 8
        set_8values_lists(l_2d, num)
        write_lists(sheet2, l_1d, 0, 1)
        remake_format(8)
    elif len(l_2d) % 7 == 0:
        num = len(l_2d) // 7
        set_7values_lists(l_2d, num)
        write_lists(sheet2, l_1d, 0, 1)
        remake_format(8)
    elif len(l_2d) % 7 < len(l_2d) // 7:
        num = len(l_2d) // 8 - (7 - len(l_2d) % 8)
        num2 = 8 - len(l_2d) % 8
        set_8values_lists(l_2d,num)
        set_7values_lists(l_2d,num2)
        write_lists(sheet2, l_1d, 0, 1)
        remake_format(8)
    else:
        print("8人もしくは7人でレーンが組めません。Sheet1にデータを追加するか削除してください。")

                
    wb.save(r'./static/uploads/%s' % filename)
