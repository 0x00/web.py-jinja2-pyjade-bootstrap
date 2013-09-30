from jinja2 import Environment, PackageLoader
jinja_env = Environment(loader=PackageLoader('app', 'views'),extensions=['pyjade.ext.jinja.PyJadeExtension'])

def load(filename):
  return jinja_env.get_template(filename)


