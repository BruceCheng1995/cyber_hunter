import fire
import cyber_visual

def hello(name="World"):
  return "Hello %s!" % name

if __name__ == '__main__':
  fire.Fire(hello)
  fire.Fire(cyber_visual.cyberVisual)