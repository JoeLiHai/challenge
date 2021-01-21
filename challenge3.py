
# 寫一個function來做商品比較，function會接收一個data清單裝著 '麥香奶茶 2' 這樣的字串
# 字串中空格分開商品名稱跟數量，特別注意，商品名稱可以重複，重複時請把數量累加上去計數。
# 請參考下列function的例子 :
# data = ['麥香奶茶 2', '御飯糰 1', '可可 10', '麥香奶茶 1']
# 回傳   {'麥香奶茶': 3, '御飯糰': 1, '可可': 10}

def count_products(data):
	products = []
	for product in data:
		products.append(product.split(' '))
	print(products)


data = ['麥香奶茶 2', '御飯糰 1', '可可 10', '麥香奶茶 1']
count_products(data)