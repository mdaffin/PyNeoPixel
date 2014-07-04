# Contributor: Lukas Linhart <bugs@almad.net>
# Contributor: Marco Elver <marco.elver AT gmail.com>
# Maintainer : Jacob Melton <jmelton116@gmail.com>

pkgname=notifier
pkgver=0.0
pkgrel=1
pkgdesc="notifier"
arch=('any')
license=('None')
depends=('python' 'python-pyserial')
makedepends=('setuptools')
source=("notifier", "notifier.service", "setup.py")
options=(!emptydirs)

package() {
  python setup.py install --root=$pkgdir/ --optimize=1
}

md5sums=('530a0614de3a669314c3acd4995c54d5')
