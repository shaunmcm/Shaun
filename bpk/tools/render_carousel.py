import sys, importlib.util, carousel
p=sys.argv[1]; s=importlib.util.spec_from_file_location("m",p); m=importlib.util.module_from_spec(s); s.loader.exec_module(m)
print(carousel.render(m.SPEC, "out"))
