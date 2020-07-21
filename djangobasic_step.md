---


---

<h2 id="start"><strong>start</strong></h2>
<blockquote>
<p>ต้องมี python อยู่แล้ว</p>
</blockquote>
<pre><code>pip install virtualenv
virtualenv venv
venv\Scripts\activate 
</code></pre>
<blockquote>
<p>install framework</p>
</blockquote>
<pre><code>pip install django
django-admin startproject djangonautic
cd djangonautic
python manage.py runserver
</code></pre>
<blockquote>
<p>เริ่มใช้ app</p>
</blockquote>
<pre><code>python manage.py startapp articles
</code></pre>
<blockquote>
<p>เริ่มใช้ฐานข้อมูล</p>
</blockquote>
<pre><code>python manage.py makemigrations
python manage.py migrate
python manage.py shell
</code></pre>
<blockquote>
<p>admin เพื่อเข้า database</p>
</blockquote>
<pre><code>python manage.py createsuperuser
</code></pre>
<p>อ่านเพิ่มเติมได้ที่</p>

