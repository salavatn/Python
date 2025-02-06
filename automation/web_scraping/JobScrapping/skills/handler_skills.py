from database.db_connection import session
from database.tables.skill import TableSkill
import time


skills = ['MySQL', 'PostgreSQL', 'ClickHouse', 'Redis', 'PostgreSQL', 'MongoDB', 'FastAPI', 'Django', 
          'Flask', 'Pyramid', 'Tornado', 'CherryPy', 'Bottle', 'Falcon', 'web2py', 'Hug', 'Sanic', 'aiohttp', 
          'TurboGears', 'Django Rest', 'Vue.js', 'React', 'Angular', 'Svelte', 'Ember.js', 'Backbone.js', 'Polymer', 
          'Docker', 'Kubernetes', 'Docker Compose', 'Podman', 'Mesos', 'Nomad', 'OpenShift', 'NumPy', 'Pandas', 
          'Matplotlib', 'SciPy', 'Scikit-learn', 'aiohttp', 'asyncpg', 'NLTK', 'SpaCy', 'Gensim', 'TensorFlow', 
          'PyTorch', 'Keras', 'OpenCV', 'SQLAlchemy', 'Django ORM', 'PyMongo', 'Requests', 'urllib', 'Twisted', 
          'asyncio', 'Pytest', 'unittest', 'nose', 'doctest', 'Ansible', 'Terraform', 'Fabric', 'pip', 'virtualenv', 
          'conda', 'poetry', 'Git', 'Mercurial', 'SVN', 'PyCharm', 'Visual Studio Code', 'Sublime Text', 'RabbitMQ', 
          'Kafka', 'Redis']


lower_skills = [skill.lower() for skill in skills]


table = TableSkill

for skill in lower_skills:
    new_skill = table(skill=skill)
    session.add(new_skill)
    session.commit()
    print(f'Added {skill}')
    time.sleep(0.2)

