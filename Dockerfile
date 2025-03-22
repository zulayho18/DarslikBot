# Python image
FROM python:3.11

# Ishchi katalogni to‘g‘rilash
WORKDIR /app

# `requirements.txt` faylini nusxalash
COPY requirements.txt /app/requirements.txt

# Kutubxonalarni o‘rnatish
RUN pip install --no-cache-dir -r /app/requirements.txt

# Loyihani to'liq nusxalash
COPY . /app/

# Fayllarni tekshirish
RUN ls -la /app

# Django'ni ishga tushirish
CMD ["sh", "-c", "python manage.py migrate && python manage.py "]
