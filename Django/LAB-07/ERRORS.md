2023-05-15 07:34:25:34S - root - DEBUG - ScrapperHH.published: Вакансия опубликована 2 мая 2023 в Москве
2023-05-15 07:34:30:34S - root - DEBUG - ScrapperHH.published: Вакансия опубликована 27 апреля 2023 в Москве
2023-05-15 07:34:35:34S - root - DEBUG - ScrapperHH.published: Вакансия опубликована 19 апреля 2023 в Ростове-на-Дону
Traceback (most recent call last):
  File "/Users/salavat/GitHub/Python/Django/LAB-07/venv/lib/python3.11/site-packages/django/db/backends/utils.py", line 89, in _execute
    return self.cursor.execute(sql, params)
           ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
psycopg2.errors.NotNullViolation: null value in column "published" of relation "app_db_vacancies" violates not-null constraint
DETAIL:  Failing row contains (704, 79951663, Middle Python Developer, https://hh.ru/vacancy/79951663, null, null, null, null, null, 53, 184, null, 254, 1).


The above exception was the direct cause of the following exception:

Traceback (most recent call last):
  File "/Users/salavat/GitHub/Python/Django/LAB-07/job_finder/handler_scrapping.py", line 139, in <module>
    db.set_vacancy(**data)
  File "/Users/salavat/GitHub/Python/Django/LAB-07/job_finder/handler_db.py", line 204, in set_vacancy
    table.save()
  File "/Users/salavat/GitHub/Python/Django/LAB-07/venv/lib/python3.11/site-packages/django/db/models/base.py", line 814, in save
    self.save_base(
  File "/Users/salavat/GitHub/Python/Django/LAB-07/venv/lib/python3.11/site-packages/django/db/models/base.py", line 877, in save_base
    updated = self._save_table(
              ^^^^^^^^^^^^^^^^^
  File "/Users/salavat/GitHub/Python/Django/LAB-07/venv/lib/python3.11/site-packages/django/db/models/base.py", line 1020, in _save_table
    results = self._do_insert(
              ^^^^^^^^^^^^^^^^
  File "/Users/salavat/GitHub/Python/Django/LAB-07/venv/lib/python3.11/site-packages/django/db/models/base.py", line 1061, in _do_insert
    return manager._insert(
           ^^^^^^^^^^^^^^^^
  File "/Users/salavat/GitHub/Python/Django/LAB-07/venv/lib/python3.11/site-packages/django/db/models/manager.py", line 87, in manager_method
    return getattr(self.get_queryset(), name)(*args, **kwargs)
           ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "/Users/salavat/GitHub/Python/Django/LAB-07/venv/lib/python3.11/site-packages/django/db/models/query.py", line 1805, in _insert
    return query.get_compiler(using=using).execute_sql(returning_fields)
           ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "/Users/salavat/GitHub/Python/Django/LAB-07/venv/lib/python3.11/site-packages/django/db/models/sql/compiler.py", line 1820, in execute_sql
    cursor.execute(sql, params)
  File "/Users/salavat/GitHub/Python/Django/LAB-07/venv/lib/python3.11/site-packages/django/db/backends/utils.py", line 102, in execute
    return super().execute(sql, params)
           ^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "/Users/salavat/GitHub/Python/Django/LAB-07/venv/lib/python3.11/site-packages/django/db/backends/utils.py", line 67, in execute
    return self._execute_with_wrappers(
           ^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "/Users/salavat/GitHub/Python/Django/LAB-07/venv/lib/python3.11/site-packages/django/db/backends/utils.py", line 80, in _execute_with_wrappers
    return executor(sql, params, many, context)
           ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "/Users/salavat/GitHub/Python/Django/LAB-07/venv/lib/python3.11/site-packages/django/db/backends/utils.py", line 84, in _execute
    with self.db.wrap_database_errors:
  File "/Users/salavat/GitHub/Python/Django/LAB-07/venv/lib/python3.11/site-packages/django/db/utils.py", line 91, in __exit__
    raise dj_exc_value.with_traceback(traceback) from exc_value
  File "/Users/salavat/GitHub/Python/Django/LAB-07/venv/lib/python3.11/site-packages/django/db/backends/utils.py", line 89, in _execute
    return self.cursor.execute(sql, params)
           ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
django.db.utils.IntegrityError: null value in column "published" of relation "app_db_vacancies" violates not-null constraint
DETAIL:  Failing row contains (704, 79951663, Middle Python Developer, https://hh.ru/vacancy/79951663, null, null, null, null, null, 53, 184, null, 254, 1).
















2023-05-15 10:27:50:27S - root - DEBUG - ScrapperHH.published: Вакансия опубликована 1 мая 2023 в Москве
2023-05-15 10:28:14:28S - root - DEBUG - ScrapperHH.published: Вакансия опубликована 3 мая 2023 в Москве
Traceback (most recent call last):
  File "/Users/salavat/GitHub/Python/Django/LAB-07/venv/lib/python3.11/site-packages/urllib3/connectionpool.py", line 467, in _make_request
    self._validate_conn(conn)
  File "/Users/salavat/GitHub/Python/Django/LAB-07/venv/lib/python3.11/site-packages/urllib3/connectionpool.py", line 1092, in _validate_conn
    conn.connect()
  File "/Users/salavat/GitHub/Python/Django/LAB-07/venv/lib/python3.11/site-packages/urllib3/connection.py", line 635, in connect
    sock_and_verified = _ssl_wrap_socket_and_match_hostname(
                        ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "/Users/salavat/GitHub/Python/Django/LAB-07/venv/lib/python3.11/site-packages/urllib3/connection.py", line 774, in _ssl_wrap_socket_and_match_hostname
    ssl_sock = ssl_wrap_socket(
               ^^^^^^^^^^^^^^^^
  File "/Users/salavat/GitHub/Python/Django/LAB-07/venv/lib/python3.11/site-packages/urllib3/util/ssl_.py", line 459, in ssl_wrap_socket
    ssl_sock = _ssl_wrap_socket_impl(sock, context, tls_in_tls, server_hostname)
               ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "/Users/salavat/GitHub/Python/Django/LAB-07/venv/lib/python3.11/site-packages/urllib3/util/ssl_.py", line 503, in _ssl_wrap_socket_impl
    return ssl_context.wrap_socket(sock, server_hostname=server_hostname)
           ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "/Users/salavat/.pyenv/versions/3.11.3/lib/python3.11/ssl.py", line 517, in wrap_socket
    return self.sslsocket_class._create(
           ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "/Users/salavat/.pyenv/versions/3.11.3/lib/python3.11/ssl.py", line 1075, in _create
    self.do_handshake()
  File "/Users/salavat/.pyenv/versions/3.11.3/lib/python3.11/ssl.py", line 1346, in do_handshake
    self._sslobj.do_handshake()
TimeoutError: [Errno 60] Operation timed out

The above exception was the direct cause of the following exception:

Traceback (most recent call last):
  File "/Users/salavat/GitHub/Python/Django/LAB-07/venv/lib/python3.11/site-packages/requests/adapters.py", line 486, in send
    resp = conn.urlopen(
           ^^^^^^^^^^^^^
  File "/Users/salavat/GitHub/Python/Django/LAB-07/venv/lib/python3.11/site-packages/urllib3/connectionpool.py", line 844, in urlopen
    retries = retries.increment(
              ^^^^^^^^^^^^^^^^^^
  File "/Users/salavat/GitHub/Python/Django/LAB-07/venv/lib/python3.11/site-packages/urllib3/util/retry.py", line 470, in increment
    raise reraise(type(error), error, _stacktrace)
          ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "/Users/salavat/GitHub/Python/Django/LAB-07/venv/lib/python3.11/site-packages/urllib3/util/util.py", line 39, in reraise
    raise value
  File "/Users/salavat/GitHub/Python/Django/LAB-07/venv/lib/python3.11/site-packages/urllib3/connectionpool.py", line 790, in urlopen
    response = self._make_request(
               ^^^^^^^^^^^^^^^^^^^
  File "/Users/salavat/GitHub/Python/Django/LAB-07/venv/lib/python3.11/site-packages/urllib3/connectionpool.py", line 491, in _make_request
    raise new_e
  File "/Users/salavat/GitHub/Python/Django/LAB-07/venv/lib/python3.11/site-packages/urllib3/connectionpool.py", line 469, in _make_request
    self._raise_timeout(err=e, url=url, timeout_value=conn.timeout)
  File "/Users/salavat/GitHub/Python/Django/LAB-07/venv/lib/python3.11/site-packages/urllib3/connectionpool.py", line 370, in _raise_timeout
    raise ReadTimeoutError(
urllib3.exceptions.ReadTimeoutError: HTTPSConnectionPool(host='hh.ru', port=443): Read timed out. (read timeout=None)

During handling of the above exception, another exception occurred:

Traceback (most recent call last):
  File "/Users/salavat/GitHub/Python/Django/LAB-07/job_finder/handler_scrapping.py", line 76, in <module>
    job_posted   = hh.get_job_posted(job_link=job_link)
                   ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "/Users/salavat/GitHub/Python/Django/LAB-07/job_finder/app_webscrapping/scrapper_hh.py", line 150, in get_job_posted
    response   = requests.get(job_link, headers=headers)
                 ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "/Users/salavat/GitHub/Python/Django/LAB-07/venv/lib/python3.11/site-packages/requests/api.py", line 73, in get
    return request("get", url, params=params, **kwargs)
           ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "/Users/salavat/GitHub/Python/Django/LAB-07/venv/lib/python3.11/site-packages/requests/api.py", line 59, in request
    return session.request(method=method, url=url, **kwargs)
           ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "/Users/salavat/GitHub/Python/Django/LAB-07/venv/lib/python3.11/site-packages/requests/sessions.py", line 587, in request
    resp = self.send(prep, **send_kwargs)
           ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "/Users/salavat/GitHub/Python/Django/LAB-07/venv/lib/python3.11/site-packages/requests/sessions.py", line 701, in send
    r = adapter.send(request, **kwargs)
        ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "/Users/salavat/GitHub/Python/Django/LAB-07/venv/lib/python3.11/site-packages/requests/adapters.py", line 532, in send
    raise ReadTimeout(e, request=request)
requests.exceptions.ReadTimeout: HTTPSConnectionPool(host='hh.ru', port=443): Read timed out. (read timeout=None)