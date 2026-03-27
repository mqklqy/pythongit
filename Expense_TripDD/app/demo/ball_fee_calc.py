site_fee = 116  # float(input('请输入场地费:')) 场地费
ball_fee = 50  # float(input('请输入球费:'))    球费
organizers_count_m = 1  # 组织者男人数 A费用除外
organizers_count_f = 0  # 组织者女人数 A费用除外
male_count = 4  # 男数
female_count = 3  # 女数
female_discount = 5  # 女生优惠5元/次

total_cost = site_fee + ball_fee
print('*****************************************')
print('场地费:{}元'.format(site_fee))
print('球费:{}元'.format(ball_fee))
print('活动总费用:{}元'.format(total_cost))
print('参与人数共{}人(男{},女{})'.format(male_count + female_count, male_count, female_count))
male_cost = round((total_cost + female_discount * female_count) / (male_count + female_count), 2)
female_cost = round(male_cost - female_discount, 2)
print('女生减{}元/次'.format(female_discount))
print('男生人均{}元'.format(male_cost))
print('女生人均{}元'.format(female_cost))
print('*****************************************')
print('男生A总金额{}元'.format(male_cost * (male_count - organizers_count_m)))
print('女生A总金额{}元'.format(female_cost * (female_count - organizers_count_f)))
