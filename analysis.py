import pandas

df1 = pandas.read_csv('final.csv')
df2 = df1[['matched_num'],['user_name']]

df3 = pandas.DataFrame(df1, columns=['matched_num'])
print(df3)
df4 = df3.merge(df1)
print df4
#print(df3.join(df1,['matched_num'],'left'))
df4.to_csv('out.csv')


#print(df2)
