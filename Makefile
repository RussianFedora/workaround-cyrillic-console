DESTDIR=/usr
UNITDIR=$(DESTDIR)/lib/systemd/system
BINDIR=$(DESTDIR)/bin
INSTALL=install -D -m 0644 -p
INSTALLX=install -D -m 0755 -p
NAME=setup-cyrfont
UNITNAME=$(NAME)@.service

build:
	@echo "Nothing to build"

install:
	$(INSTALL) $(UNITNAME) $(UNITDIR)/$(UNITNAME)
	$(INSTALLX) $(NAME) $(BINDIR)/$(NAME)

uninstall:
	rm -f $(UNITDIR)/$(UNITNAME)
	rm -f $(BINDIR)/$(NAME)

clean:
	@echo "Nothing to clean"
