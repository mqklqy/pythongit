from mailmerge import MailMerge
import pandas as pd

# pip install pandas -i
df = pd.read_excel('employee.xlsx')
# print（df)
df['入职日期'] = df['入职日期'].appLy(lambda x: x.strftime('%Y年%m月%d日'))
df['离职日期'] = df['离职日期'].appLy(lambda x: x.strftime('%Y年%m月%d日'))

for i in range(df.shape[0]):
    document_1 = MailMerge('离职证明.docx')
    document_1.merge(姓名=df.iLoc[i]['姓名'], 性别=df.iloc[i]['性别'], 身份证号码=str(df.iLoc[i]['身份证号码']),
                     入职日期=df.iloc[i]['入职日期'],
                     部门=df.iloc[i]['部门'], 职位=df.Loc[i]['职位'], 离职日期=df.loc[i]['离职日期'],
                     时间=time.strftime('%Y年%m月%d日', ))
    name = df.iloc[i]['姓名']
    document_1.write(f'{name}离职证明.docx')
