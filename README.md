<h3 tabindex="-1" class="heading-element" dir="auto"><font style="vertical-align: inherit;"><font style="vertical-align: inherit;">
Проектное руководство по созданию современных API с Django и Django REST Framework по книге  Уильяма С. Винсента "Django for APIs"
</font></font></h3>
<div class="markdown-heading" dir="auto"><h2 tabindex="-1" class="heading-element" dir="auto"><font style="vertical-align: inherit;"><font style="vertical-align: inherit;">Установка</font></font></h2><a id="user-
content-installation" class="anchor" aria-label="Постоянная ссылка: Установка" href="#installation"><svg class="octicon octicon-link" viewBox="0 0 16 16" version="1.1" width="16" height="16" aria-hidden="true">
</svg></a></div>
<ul>
  <li>
    <strong><font style="vertical-align: inherit;"><font style="vertical-align: inherit;">Шаг 1</font></font></strong>
    <font style="vertical-align: inherit;"><font style="vertical-align: inherit;"> : Клонируйте исходный код с GitHub</font></font>
  </li>
  <div class="snippet-clipboard-content notranslate position-relative overflow-auto"><pre class="notranslate"><code>git clone https://github.com/Viktoriya472/Drf.git
 </code></pre>
    <div class="zeroclipboard-container">
      <clipboard-copy aria-label="Copy" class="ClipboardButton btn btn-invisible js-clipboard-copy m-2 p-0 d-flex flex-justify-center flex-items-center" data-copy-feedback="Copied!" data-tooltip-direction="w" 
        value="git clone https://github.com/Viktoriya472/Drf.git" tabindex="0" role="button">
        <svg aria-hidden="true" height="16" viewBox="0 0 16 16" version="1.1" width="16" data-view-component="true" class="octicon octicon-copy js-clipboard-copy-icon"></svg>
        <svg aria-hidden="true" height="16" viewBox="0 0 16 16" version="1.1" width="16" data-view-component="true" class="octicon octicon-check js-clipboard-check-icon color-fg-success d-none"></svg>
      </clipboard-copy>
    </div>
  </div>
  <li><strong><font style="vertical-align: inherit;"><font style="vertical-align: inherit;">Шаг 2</font></font></strong>
    <font style="vertical-align: inherit;"><font style="vertical-align: inherit;"> : Создайте и используйте виртуальную среду (python 3.11) с помощью </font></font><code>venv</code>
  </li>
  <div class="snippet-clipboard-content notranslate position-relative overflow-auto"><pre class="notranslate"><code>python -m venv .venv
.venv/scripts/activate</code></pre>
    <div class="zeroclipboard-container">
      <clipboard-copy aria-label="Copy" class="ClipboardButton btn btn-invisible js-clipboard-copy m-2 p-0 d-flex flex-justify-center flex-items-center" data-copy-feedback="Copied!" data-tooltip-direction="w"
        value="python -m venv .venv
.venv/scripts/activate" tabindex="0" role="button">
        <svg aria-hidden="true" height="16" viewBox="0 0 16 16" version="1.1" width="16" data-view-component="true" class="octicon octicon-copy js-clipboard-copy-icon"></svg>
        <svg aria-hidden="true" height="16" viewBox="0 0 16 16" version="1.1" width="16" data-view-component="true" class="octicon octicon-check js-clipboard-check-icon color-fg-success d-none"></svg>
      </clipboard-copy>
    </div>
  </div>
  <li>
    <strong><font style="vertical-align: inherit;"><font style="vertical-align: inherit;">Шаг 3</font></font></strong>
    <font style="vertical-align: inherit;"><font style="vertical-align: inherit;"> : Установите зависимости проекта</font></font>
  </li>
<div class="snippet-clipboard-content notranslate position-relative overflow-auto"><pre class="notranslate"><code>cd .\Drf\
pip install -r req.txt</code></pre>
    <div class="zeroclipboard-container">
      <clipboard-copy aria-label="Copy" class="ClipboardButton btn btn-invisible js-clipboard-copy m-2 p-0 d-flex flex-justify-center flex-items-center" data-copy-feedback="Copied!" data-tooltip-direction="w"
        value="cd .\Drf\
pip install -r req.txt" tabindex="0" role="button">
        <svg aria-hidden="true" height="16" viewBox="0 0 16 16" version="1.1" width="16" data-view-component="true" class="octicon octicon-copy js-clipboard-copy-icon"></svg>
        <svg aria-hidden="true" height="16" viewBox="0 0 16 16" version="1.1" width="16" data-view-component="true" class="octicon octicon-check js-clipboard-check-icon color-fg-success d-none"></svg>
      </clipboard-copy>
    </div>
  </div>
  <li>
  <strong><font style="vertical-align: inherit;"><font style="vertical-align: inherit;">Шаг 4</font></font></strong>
  <font style="vertical-align: inherit;"><font style="vertical-align: inherit;"> : Запустите сервер</font></font>
  </li>
    <div class="snippet-clipboard-content notranslate position-relative overflow-auto"><pre class="notranslate"><code>python manage.py runserver
 </code></pre><div class="zeroclipboard-container">
    <clipboard-copy aria-label="Copy" class="ClipboardButton btn btn-invisible js-clipboard-copy m-2 p-0 d-flex flex-justify-center flex-items-center" data-copy-feedback="Copied!" data-tooltip-direction="w" 
      value="python manage.py runserver" tabindex="0" role="button">
      <svg aria-hidden="true" height="16" viewBox="0 0 16 16" version="1.1" width="16" data-view-component="true" class="octicon octicon-copy js-clipboard-copy-icon"></svg>
      <svg aria-hidden="true" height="16" viewBox="0 0 16 16" version="1.1" width="16" data-view-component="true" class="octicon octicon-check js-clipboard-check-icon color-fg-success d-none"></svg>
    </clipboard-copy>
  </div>
  </div>
  <pre>
    <ul dir="auto">
      <li><font style="vertical-align: inherit;"><font style="vertical-align: inherit;">регистрация - </font></font><a href="http://127.0.0.1:8000/api/v1/dj-rest-auth/registration/" rel="nofollow"><font style="vertical-align: inherit;"><font style="vertical-align: inherit;">http://127.0.0.1:8000/api/v1/dj-rest-auth/registration/</font></font></a></li>
      <li><font style="vertical-align: inherit;"><font style="vertical-align: inherit;">вход - </font></font><a href="http://127.0.0.1:8000/api/v1/dj-rest-auth/login/" rel="nofollow"><font style="vertical-align: inherit;"><font style="vertical-align: inherit;">http://127.0.0.1:8000/api/v1/dj-rest-auth/login/</font></font></a></li>
      <li><font style="vertical-align: inherit;"><font style="vertical-align: inherit;">все посты - </font></font><a href="http://127.0.0.1:8000/api/v1/" rel="nofollow"><font style="vertical-align: inherit;"><font style="vertical-align: inherit;">http://127.0.0.1:8000/api/v1/</font></font></a></li>
      <li><font style="vertical-align: inherit;"><font style="vertical-align: inherit;">все пользователи - </font></font><a href="http://127.0.0.1:8000/api/v1/users/" rel="nofollow"><font style="vertical-align: inherit;"><font style="vertical-align: inherit;">http://127.0.0.1:8000/api/v1/users/</font></font></a></li>
      <li><font style="vertical-align: inherit;"><font style="vertical-align: inherit;">выход из системы - </font></font><a href="http://127.0.0.1:8000/api/v1/dj-rest-auth/logout/" rel="nofollow"><font style="vertical-align: inherit;"><font style="vertical-align: inherit;">http://127.0.0.1:8000/api/v1/dj-rest-auth/logout/</font></font></a></li>
    </ul>
 </pre>
  
</ul>
