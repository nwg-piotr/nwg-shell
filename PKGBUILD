# Maintainer: Piotr Miller <nwg.piotr@gmail.com>
pkgname=('nwg-shell')
pkgver=0.0.1
pkgrel=1
pkgdesc="nwg-shell meta-package and installer"
arch=('x86_64')
url="https://github.com/nwg-piotr/nwg-shell"
license=('MIT')
depends=('python' 'sway' 'grim' 'slurp' 'swayidle' 'swaylock' 'swappy' 'wl-clipboard' 'jq'
         'lxappearance' 'foot' 'wlsunset' 'wdisplays' 'swaync' 'python-geopy' 'python-dasbus'
         'azote' 'autotiling' 'nwg-panel' 'nwg-wrapper' 'nwg-bar' 'nwg-dock' 'nwg-drawer'
         'nwg-menu' 'gopsuinfo' 'nwg-shell-config')
makedepends=('python-setuptools' 'python-wheel')
source=("$pkgname-$pkgver.tar.gz::https://github.com/nwg-piotr/nwg-shell/archive/v"$pkgver".tar.gz")

md5sums=('de516b836cf6bbf7aae2c1dd321986d9')

package() {
  cd "${pkgname}-${pkgver}"
  python setup.py install --root="${pkgdir}" --optimize=1
}
