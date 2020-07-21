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
<p>python <a href="http://manage.py">manage.py</a> startapp articles</p>
<blockquote>
<p>เริ่มใช้ฐานข้อมูล</p>
</blockquote>
<p>python <a href="http://manage.py">manage.py</a> makemigrations<br>
python <a href="http://manage.py">manage.py</a> migrate<br>
python <a href="http://manage.py">manage.py</a> shell</p>
<blockquote>
<p>admin เพื่อเข้า database</p>
</blockquote>
<p>python <a href="http://manage.py">manage.py</a> createsuperuser</p>

