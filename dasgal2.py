# Дэлгүүрүүдийн өгөгдөл
name1, fruit_kg1, fruit_price1, retail_fruit_price1, retail_other_price1 = "Бамбарууш", 534, 5000, 487, 12
name2, fruit_kg2, fruit_price2, retail_fruit_price2, retail_other_price2 = "Жимсэн", 764, 4800, 423, 14
name3, fruit_kg3, fruit_price3, retail_fruit_price3, retail_other_price3 = "Fruits", 136, 3000, 8000, 0

# Орлого тооцоолох
income1 = fruit_kg1 * retail_fruit_price1 + fruit_price1 * retail_other_price1
income2 = fruit_kg2 * retail_fruit_price2 + fruit_price2 * retail_other_price2
income3 = fruit_kg3 * retail_fruit_price3 + fruit_price3 * retail_other_price3

# Бүх дэлгүүрийн нийт орлого
total_income = income1 + income2 + income3

# Үр дүн хэвлэх
print(f"{name1} дэлгүүрийн орлого: {income1}")
print(f"{name2} дэлгүүрийн орлого: {income2}")
print(f"{name3} дэлгүүрийн орлого: {income3}")
print(f"Нийт борлуулалтын орлого: {total_income}")
