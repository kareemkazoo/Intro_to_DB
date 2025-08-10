import mysql.connector
from mysql.connector import Error

try:
    # محاولة الاتصال بالسيرفر (غير البيانات حسب إعداداتك)
    connection = mysql.connector.connect(
        host='localhost',      # أو IP السيرفر
        user='root',           # اسم المستخدم
        password='Kazo@2050@'  # كلمة المرور
    )

    if connection.is_connected():
        cursor = connection.cursor()
        # إنشاء قاعدة البيانات لو مش موجودة
        cursor.execute("CREATE DATABASE IF NOT EXISTS alx_book_store")
        print("Database 'alx_book_store' created successfully!")

except Error as e:
    print(f"Error while connecting to MySQL: {e}")

finally:
    # إغلاق الكيرسر والاتصال
    if 'cursor' in locals() and cursor:
        cursor.close()
    if 'connection' in locals() and connection.is_connected():
        connection.close()
