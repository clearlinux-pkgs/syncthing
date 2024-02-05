#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
# Using build pattern: make
# autospec version: v3
# autospec commit: 750e50d
#
# Source0 file verified with key 0xD26E6ED000654A3E (release@syncthing.net)
#
Name     : syncthing
Version  : 1.27.2
Release  : 11
URL      : https://github.com/syncthing/syncthing/releases/download/v1.27.2/syncthing-source-v1.27.2.tar.gz
Source0  : https://github.com/syncthing/syncthing/releases/download/v1.27.2/syncthing-source-v1.27.2.tar.gz
Source1  : https://github.com/syncthing/syncthing/releases/download/v1.27.2/syncthing-source-v1.27.2.tar.gz.asc
Summary  : No detailed summary available
Group    : Development/Tools
License  : Apache-2.0 BSD-2-Clause BSD-3-Clause ISC MIT MPL-2.0 MPL-2.0-no-copyleft-exception
Requires: syncthing-bin = %{version}-%{release}
Requires: syncthing-config = %{version}-%{release}
Requires: syncthing-data = %{version}-%{release}
Requires: syncthing-license = %{version}-%{release}
Requires: syncthing-man = %{version}-%{release}
Requires: syncthing-services = %{version}-%{release}
BuildRequires : go
BuildRequires : llvm
# Suppress stripping binaries
%define __strip /bin/true
%define debug_package %{nil}

%description
The Snappy compression format in the Go programming language.
To download and install from source:
$ go get github.com/golang/snappy

%package bin
Summary: bin components for the syncthing package.
Group: Binaries
Requires: syncthing-data = %{version}-%{release}
Requires: syncthing-config = %{version}-%{release}
Requires: syncthing-license = %{version}-%{release}
Requires: syncthing-services = %{version}-%{release}

%description bin
bin components for the syncthing package.


%package config
Summary: config components for the syncthing package.
Group: Default

%description config
config components for the syncthing package.


%package data
Summary: data components for the syncthing package.
Group: Data

%description data
data components for the syncthing package.


%package license
Summary: license components for the syncthing package.
Group: Default

%description license
license components for the syncthing package.


%package man
Summary: man components for the syncthing package.
Group: Default

%description man
man components for the syncthing package.


%package services
Summary: services components for the syncthing package.
Group: Systemd services
Requires: systemd

%description services
services components for the syncthing package.


%prep
%setup -q -n syncthing
cd %{_builddir}/syncthing
pushd ..
cp -a syncthing buildavx2
popd

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
export SOURCE_DATE_EPOCH=1707106581
export GCC_IGNORE_WERROR=1
export CC=clang
export CXX=clang++
export LD=ld.gold
CLEAR_INTERMEDIATE_CFLAGS=${CLEAR_ORIG_CFLAGS/ -Wa,/ -fno-integrated-as -Wa,}
CLEAR_INTERMEDIATE_CXXFLAGS=${CLEAR_ORIG_CXXFLAGS/ -Wa,/ -fno-integrated-as -Wa,}
export AR=llvm-ar
export RANLIB=llvm-ranlib
export NM=llvm-nm
CLEAR_INTERMEDIATE_CFLAGS="$CLEAR_INTERMEDIATE_CFLAGS -O3 -ffat-lto-objects -flto "
CLEAR_INTERMEDIATE_FCFLAGS="$CLEAR_INTERMEDIATE_FFLAGS -O3 -ffat-lto-objects -flto "
CLEAR_INTERMEDIATE_FFLAGS="$CLEAR_INTERMEDIATE_FFLAGS -O3 -ffat-lto-objects -flto "
CLEAR_INTERMEDIATE_CXXFLAGS="$CLEAR_INTERMEDIATE_CXXFLAGS -O3 -ffat-lto-objects -flto "
CFLAGS="$CLEAR_INTERMEDIATE_CFLAGS"
CXXFLAGS="$CLEAR_INTERMEDIATE_CXXFLAGS"
FFLAGS="$CLEAR_INTERMEDIATE_FFLAGS"
FCFLAGS="$CLEAR_INTERMEDIATE_FCFLAGS"
ASFLAGS="$CLEAR_INTERMEDIATE_ASFLAGS"
LDFLAGS="$CLEAR_INTERMEDIATE_LDFLAGS"
go run build.go -no-upgrade build syncthing  %{?_smp_mflags}

pushd ../buildavx2
CFLAGS="$CLEAR_INTERMEDIATE_CFLAGS -march=x86-64-v3 -Wl,-z,x86-64-v3 "
CXXFLAGS="$CLEAR_INTERMEDIATE_CXXFLAGS -march=x86-64-v3 -Wl,-z,x86-64-v3 "
FFLAGS="$CLEAR_INTERMEDIATE_FFLAGS -march=x86-64-v3 -Wl,-z,x86-64-v3 "
FCFLAGS="$CLEAR_INTERMEDIATE_FCFLAGS -march=x86-64-v3 "
LDFLAGS="$CLEAR_INTERMEDIATE_LDFLAGS -march=x86-64-v3 "
go run build.go -no-upgrade build syncthing  %{?_smp_mflags}
popd

%check
export LANG=C.UTF-8
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
go run build.go test syncthing

%install
export GCC_IGNORE_WERROR=1
export CC=clang
export CXX=clang++
export LD=ld.gold
CLEAR_INTERMEDIATE_CFLAGS=${CLEAR_ORIG_CFLAGS/ -Wa,/ -fno-integrated-as -Wa,}
CLEAR_INTERMEDIATE_CXXFLAGS=${CLEAR_ORIG_CXXFLAGS/ -Wa,/ -fno-integrated-as -Wa,}
export AR=llvm-ar
export RANLIB=llvm-ranlib
export NM=llvm-nm
CLEAR_INTERMEDIATE_CFLAGS="$CLEAR_INTERMEDIATE_CFLAGS -O3 -ffat-lto-objects -flto "
CLEAR_INTERMEDIATE_FCFLAGS="$CLEAR_INTERMEDIATE_FFLAGS -O3 -ffat-lto-objects -flto "
CLEAR_INTERMEDIATE_FFLAGS="$CLEAR_INTERMEDIATE_FFLAGS -O3 -ffat-lto-objects -flto "
CLEAR_INTERMEDIATE_CXXFLAGS="$CLEAR_INTERMEDIATE_CXXFLAGS -O3 -ffat-lto-objects -flto "
CFLAGS="$CLEAR_INTERMEDIATE_CFLAGS"
CXXFLAGS="$CLEAR_INTERMEDIATE_CXXFLAGS"
FFLAGS="$CLEAR_INTERMEDIATE_FFLAGS"
FCFLAGS="$CLEAR_INTERMEDIATE_FCFLAGS"
ASFLAGS="$CLEAR_INTERMEDIATE_ASFLAGS"
LDFLAGS="$CLEAR_INTERMEDIATE_LDFLAGS"
export SOURCE_DATE_EPOCH=1707106581
rm -rf %{buildroot}
mkdir -p %{buildroot}/usr/share/package-licenses/syncthing
cp %{_builddir}/syncthing/LICENSE %{buildroot}/usr/share/package-licenses/syncthing/d7e3ed5ac149ac1e2d2e0f4daff081c1dafef1c0 || :
cp %{_builddir}/syncthing/cmd/strelaypoolsrv/LICENSE %{buildroot}/usr/share/package-licenses/syncthing/694bed385b0e246185c61a1d991a7fd92471930b || :
cp %{_builddir}/syncthing/cmd/strelaysrv/LICENSE %{buildroot}/usr/share/package-licenses/syncthing/694bed385b0e246185c61a1d991a7fd92471930b || :
cp %{_builddir}/syncthing/gui/default/vendor/angular/angular-dirPagination.js.LICENSE %{buildroot}/usr/share/package-licenses/syncthing/7d1bc92f0ee5987fd034a5a8ea664b35236736fc || :
cp %{_builddir}/syncthing/gui/default/vendor/angular/angular-sanitize.js.LICENSE %{buildroot}/usr/share/package-licenses/syncthing/4539e1c1452683731710f1867fff6d5d148b0c86 || :
cp %{_builddir}/syncthing/gui/default/vendor/angular/angular-translate-loader-static-files.js.LICENSE %{buildroot}/usr/share/package-licenses/syncthing/fa644321f4cb0aadb2bd05f398d4a23ae563128b || :
cp %{_builddir}/syncthing/gui/default/vendor/angular/angular-translate.js.LICENSE %{buildroot}/usr/share/package-licenses/syncthing/fa644321f4cb0aadb2bd05f398d4a23ae563128b || :
cp %{_builddir}/syncthing/gui/default/vendor/angular/angular.js.LICENSE %{buildroot}/usr/share/package-licenses/syncthing/4539e1c1452683731710f1867fff6d5d148b0c86 || :
cp %{_builddir}/syncthing/gui/default/vendor/bootstrap/LICENSE %{buildroot}/usr/share/package-licenses/syncthing/13581bcb019974856e6ab27e6072b7ab22c100db || :
cp %{_builddir}/syncthing/gui/default/vendor/daterangepicker/LICENSE %{buildroot}/usr/share/package-licenses/syncthing/e0b761db9d0831cae676bcb303fc7d9095ae9beb || :
cp %{_builddir}/syncthing/gui/default/vendor/fancytree/LICENSE.txt %{buildroot}/usr/share/package-licenses/syncthing/219c5dccdc6fb5f0e047ca6ce8e0228f12e90017 || :
cp %{_builddir}/syncthing/gui/default/vendor/jquery/LICENSE %{buildroot}/usr/share/package-licenses/syncthing/174f178b9e4dcfa220b6a12ada1b869e8a6684b1 || :
cp %{_builddir}/syncthing/gui/default/vendor/moment/LICENSE %{buildroot}/usr/share/package-licenses/syncthing/aab97739ef7d50750adbc9ffbfd1cbf9608eb678 || :
cp %{_builddir}/syncthing/lib/logger/LICENSE %{buildroot}/usr/share/package-licenses/syncthing/a4c50f5c034ae8ad818e6f5773a7d65e03b58b37 || :
cp %{_builddir}/syncthing/lib/protocol/LICENSE %{buildroot}/usr/share/package-licenses/syncthing/59e0fe537bc596157e3417e3ff4038a26f579393 || :
cp %{_builddir}/syncthing/next-gen-gui/LICENSE %{buildroot}/usr/share/package-licenses/syncthing/d7e3ed5ac149ac1e2d2e0f4daff081c1dafef1c0 || :
cp %{_builddir}/syncthing/vendor/github.com/AudriusButkevicius/recli/LICENSE %{buildroot}/usr/share/package-licenses/syncthing/d22157abc0fc0b4ae96380c09528e23cf77290a9 || :
cp %{_builddir}/syncthing/vendor/github.com/Azure/go-ntlmssp/LICENSE %{buildroot}/usr/share/package-licenses/syncthing/90778a2b78620d46a521986f99136e44a1dde89f || :
cp %{_builddir}/syncthing/vendor/github.com/alecthomas/kong/COPYING %{buildroot}/usr/share/package-licenses/syncthing/78af3b5baa64be2c32fecd3ef812aee13904da2a || :
cp %{_builddir}/syncthing/vendor/github.com/beorn7/perks/LICENSE %{buildroot}/usr/share/package-licenses/syncthing/b2e4520feb0f9b51ad373256b94c3faf4c1e6871 || :
cp %{_builddir}/syncthing/vendor/github.com/calmh/xdr/LICENSE %{buildroot}/usr/share/package-licenses/syncthing/428e62f9df892db59cde7dba84a1f37c49bd4252 || :
cp %{_builddir}/syncthing/vendor/github.com/ccding/go-stun/LICENSE %{buildroot}/usr/share/package-licenses/syncthing/172ca3bbafe312a1cf09cfff26953db2f425c28e || :
cp %{_builddir}/syncthing/vendor/github.com/certifi/gocertifi/LICENSE %{buildroot}/usr/share/package-licenses/syncthing/9744cedce099f727b327cd9913a1fdc58a7f5599 || :
cp %{_builddir}/syncthing/vendor/github.com/cespare/xxhash/v2/LICENSE.txt %{buildroot}/usr/share/package-licenses/syncthing/7be82c1a81e7197640a88df91dc82d64b77c7acd || :
cp %{_builddir}/syncthing/vendor/github.com/chmduquesne/rollinghash/LICENSE.txt %{buildroot}/usr/share/package-licenses/syncthing/4b23a2c0bf17e7644903958716e8e01967aa874c || :
cp %{_builddir}/syncthing/vendor/github.com/cpuguy83/go-md2man/v2/LICENSE.md %{buildroot}/usr/share/package-licenses/syncthing/b7a606730713ac061594edab33cf941704b4a95c || :
cp %{_builddir}/syncthing/vendor/github.com/d4l3k/messagediff/LICENSE %{buildroot}/usr/share/package-licenses/syncthing/039965feff6efd8f281c4d4989a2547a27c9270c || :
cp %{_builddir}/syncthing/vendor/github.com/flynn-archive/go-shlex/COPYING %{buildroot}/usr/share/package-licenses/syncthing/2b8b815229aa8a61e483fb4ba0588b8b6c491890 || :
cp %{_builddir}/syncthing/vendor/github.com/getsentry/raven-go/LICENSE %{buildroot}/usr/share/package-licenses/syncthing/6db801a1f89a986850ad801057410db22a968998 || :
cp %{_builddir}/syncthing/vendor/github.com/go-asn1-ber/asn1-ber/LICENSE %{buildroot}/usr/share/package-licenses/syncthing/e9e85ffe1ad083ba47b7c72f5553c3368a655872 || :
cp %{_builddir}/syncthing/vendor/github.com/go-ldap/ldap/v3/LICENSE %{buildroot}/usr/share/package-licenses/syncthing/26bee26046eaa07afedc723e392fcc1341d86739 || :
cp %{_builddir}/syncthing/vendor/github.com/go-ole/go-ole/LICENSE %{buildroot}/usr/share/package-licenses/syncthing/565471fdf06cfb21b7c69c5fc329a1341d5d9ad0 || :
cp %{_builddir}/syncthing/vendor/github.com/go-task/slim-sprig/LICENSE.txt %{buildroot}/usr/share/package-licenses/syncthing/535e3badf5b532d842627b504976fbb93bc2d8b8 || :
cp %{_builddir}/syncthing/vendor/github.com/gobwas/glob/LICENSE %{buildroot}/usr/share/package-licenses/syncthing/1b2d963c77ddfc6454ca369fc4884e87e256a2e1 || :
cp %{_builddir}/syncthing/vendor/github.com/gogo/protobuf/LICENSE %{buildroot}/usr/share/package-licenses/syncthing/06b27345acae9303e13dde9974d2b2e318b05989 || :
cp %{_builddir}/syncthing/vendor/github.com/golang/snappy/LICENSE %{buildroot}/usr/share/package-licenses/syncthing/b7b97d84a5f0b778ab971d2afce44f47c8b6e80a || :
cp %{_builddir}/syncthing/vendor/github.com/google/pprof/LICENSE %{buildroot}/usr/share/package-licenses/syncthing/2b8b815229aa8a61e483fb4ba0588b8b6c491890 || :
cp %{_builddir}/syncthing/vendor/github.com/google/uuid/LICENSE %{buildroot}/usr/share/package-licenses/syncthing/08021ae73f58f423dd6e7b525e81cf2520f7619e || :
cp %{_builddir}/syncthing/vendor/github.com/greatroar/blobloom/LICENSE %{buildroot}/usr/share/package-licenses/syncthing/2b8b815229aa8a61e483fb4ba0588b8b6c491890 || :
cp %{_builddir}/syncthing/vendor/github.com/hashicorp/golang-lru/v2/LICENSE %{buildroot}/usr/share/package-licenses/syncthing/90857ae97e892cea98fe28613afba3366d56bbf3 || :
cp %{_builddir}/syncthing/vendor/github.com/hashicorp/golang-lru/v2/simplelru/LICENSE_list %{buildroot}/usr/share/package-licenses/syncthing/bf88cc725ad09db6991d26b4af7cc790ef52c6fb || :
cp %{_builddir}/syncthing/vendor/github.com/jackpal/gateway/LICENSE %{buildroot}/usr/share/package-licenses/syncthing/b90cbf29c01e677d454e9aabdc0bd4c0887778c5 || :
cp %{_builddir}/syncthing/vendor/github.com/jackpal/go-nat-pmp/LICENSE %{buildroot}/usr/share/package-licenses/syncthing/fe47bb31aed90010edbbd000a09abb9eea90b329 || :
cp %{_builddir}/syncthing/vendor/github.com/julienschmidt/httprouter/LICENSE %{buildroot}/usr/share/package-licenses/syncthing/e0b06b4bbfdf1ffba0edaaf4aefb22922df8561e || :
cp %{_builddir}/syncthing/vendor/github.com/kballard/go-shellquote/LICENSE %{buildroot}/usr/share/package-licenses/syncthing/3afc456546a3fa3e82c0d21844cd9911d7d4464b || :
cp %{_builddir}/syncthing/vendor/github.com/klauspost/cpuid/v2/LICENSE %{buildroot}/usr/share/package-licenses/syncthing/41a17a069904e6a10fa1b1bcf67c2e4d836937d1 || :
cp %{_builddir}/syncthing/vendor/github.com/lib/pq/LICENSE.md %{buildroot}/usr/share/package-licenses/syncthing/736c20a685418b27e6992d88c0959152991d33bf || :
cp %{_builddir}/syncthing/vendor/github.com/maruel/panicparse/v2/LICENSE %{buildroot}/usr/share/package-licenses/syncthing/9601f5532b9beb07d32ebf845f3a78f604bf6f27 || :
cp %{_builddir}/syncthing/vendor/github.com/matttproud/golang_protobuf_extensions/v2/LICENSE %{buildroot}/usr/share/package-licenses/syncthing/92170cdc034b2ff819323ff670d3b7266c8bffcd || :
cp %{_builddir}/syncthing/vendor/github.com/maxbrunsfeld/counterfeiter/v6/LICENSE %{buildroot}/usr/share/package-licenses/syncthing/a0c9c581a56350ef0229f375420d52d8ca68de74 || :
cp %{_builddir}/syncthing/vendor/github.com/minio/sha256-simd/LICENSE %{buildroot}/usr/share/package-licenses/syncthing/2b8b815229aa8a61e483fb4ba0588b8b6c491890 || :
cp %{_builddir}/syncthing/vendor/github.com/miscreant/miscreant.go/LICENSE.txt %{buildroot}/usr/share/package-licenses/syncthing/d78741c6ab8e4933cd2ce6686b234c450f1c3ab5 || :
cp %{_builddir}/syncthing/vendor/github.com/onsi/ginkgo/v2/LICENSE %{buildroot}/usr/share/package-licenses/syncthing/9f1b6690bcfc732123ae209c90c62f2ba80dfcb0 || :
cp %{_builddir}/syncthing/vendor/github.com/oschwald/geoip2-golang/LICENSE %{buildroot}/usr/share/package-licenses/syncthing/e23f0c9f837e16ab8a47710ad840069df16a701b || :
cp %{_builddir}/syncthing/vendor/github.com/oschwald/maxminddb-golang/LICENSE %{buildroot}/usr/share/package-licenses/syncthing/e23f0c9f837e16ab8a47710ad840069df16a701b || :
cp %{_builddir}/syncthing/vendor/github.com/pierrec/lz4/v4/LICENSE %{buildroot}/usr/share/package-licenses/syncthing/e46e6a6dce75540a865a761f00e65c78b00c5895 || :
cp %{_builddir}/syncthing/vendor/github.com/pkg/errors/LICENSE %{buildroot}/usr/share/package-licenses/syncthing/9c1bedc0d42f24c24a1bd266f3ce101a4b0579fc || :
cp %{_builddir}/syncthing/vendor/github.com/power-devops/perfstat/LICENSE %{buildroot}/usr/share/package-licenses/syncthing/88b150e4e0f2318a6316840ed631fb2cc62d5fcc || :
cp %{_builddir}/syncthing/vendor/github.com/prometheus/client_golang/LICENSE %{buildroot}/usr/share/package-licenses/syncthing/7df059597099bb7dcf25d2a9aedfaf4465f72d8d || :
cp %{_builddir}/syncthing/vendor/github.com/prometheus/client_golang/NOTICE %{buildroot}/usr/share/package-licenses/syncthing/fd6460234f122a19f21affb6d6885269340b9176 || :
cp %{_builddir}/syncthing/vendor/github.com/prometheus/client_model/LICENSE %{buildroot}/usr/share/package-licenses/syncthing/7df059597099bb7dcf25d2a9aedfaf4465f72d8d || :
cp %{_builddir}/syncthing/vendor/github.com/prometheus/common/LICENSE %{buildroot}/usr/share/package-licenses/syncthing/7df059597099bb7dcf25d2a9aedfaf4465f72d8d || :
cp %{_builddir}/syncthing/vendor/github.com/prometheus/procfs/LICENSE %{buildroot}/usr/share/package-licenses/syncthing/7df059597099bb7dcf25d2a9aedfaf4465f72d8d || :
cp %{_builddir}/syncthing/vendor/github.com/quic-go/qtls-go1-20/LICENSE %{buildroot}/usr/share/package-licenses/syncthing/d6a5f1ecaedd723c325a2063375b3517e808a2b5 || :
cp %{_builddir}/syncthing/vendor/github.com/quic-go/quic-go/LICENSE %{buildroot}/usr/share/package-licenses/syncthing/78d85619a69f25c64fad9f76fc734a66107b18d4 || :
cp %{_builddir}/syncthing/vendor/github.com/rcrowley/go-metrics/LICENSE %{buildroot}/usr/share/package-licenses/syncthing/f4f6a4a62f50348c9f4fa311fd2023d8ed32e380 || :
cp %{_builddir}/syncthing/vendor/github.com/russross/blackfriday/v2/LICENSE.txt %{buildroot}/usr/share/package-licenses/syncthing/da34754c05d40ff81f91de8c1b85ea6e5503e21d || :
cp %{_builddir}/syncthing/vendor/github.com/shirou/gopsutil/v3/LICENSE %{buildroot}/usr/share/package-licenses/syncthing/0c40e548c3768125e9fd4c09907b2457341edef6 || :
cp %{_builddir}/syncthing/vendor/github.com/syncthing/notify/LICENSE %{buildroot}/usr/share/package-licenses/syncthing/97c18dd612ad4458f3823e836adb21dd11962ac9 || :
cp %{_builddir}/syncthing/vendor/github.com/syndtr/goleveldb/LICENSE %{buildroot}/usr/share/package-licenses/syncthing/5eaad1bc8f139227bee002062efa2e1b603fb2db || :
cp %{_builddir}/syncthing/vendor/github.com/thejerf/suture/v4/LICENSE %{buildroot}/usr/share/package-licenses/syncthing/2bb1eaec43fbd55aaffe41c50270b0ec08b68be9 || :
cp %{_builddir}/syncthing/vendor/github.com/urfave/cli/LICENSE %{buildroot}/usr/share/package-licenses/syncthing/225d7794e5557038980b6f5c898175c1bac63485 || :
cp %{_builddir}/syncthing/vendor/github.com/vitrun/qart/LICENSE %{buildroot}/usr/share/package-licenses/syncthing/3d9ca858ae047e05c8c031e24b41aea21417fc2a || :
cp %{_builddir}/syncthing/vendor/github.com/vitrun/qart/LICENSE.bsd %{buildroot}/usr/share/package-licenses/syncthing/c2252212aa407a45427696985f2d8c7f774df3b2 || :
cp %{_builddir}/syncthing/vendor/github.com/yusufpapurcu/wmi/LICENSE %{buildroot}/usr/share/package-licenses/syncthing/c0f4ffe120079028c20033cf13619b9f52434c22 || :
cp %{_builddir}/syncthing/vendor/go.uber.org/mock/LICENSE %{buildroot}/usr/share/package-licenses/syncthing/2b8b815229aa8a61e483fb4ba0588b8b6c491890 || :
cp %{_builddir}/syncthing/vendor/golang.org/x/crypto/LICENSE %{buildroot}/usr/share/package-licenses/syncthing/d6a5f1ecaedd723c325a2063375b3517e808a2b5 || :
cp %{_builddir}/syncthing/vendor/golang.org/x/exp/LICENSE %{buildroot}/usr/share/package-licenses/syncthing/d6a5f1ecaedd723c325a2063375b3517e808a2b5 || :
cp %{_builddir}/syncthing/vendor/golang.org/x/mod/LICENSE %{buildroot}/usr/share/package-licenses/syncthing/d6a5f1ecaedd723c325a2063375b3517e808a2b5 || :
cp %{_builddir}/syncthing/vendor/golang.org/x/net/LICENSE %{buildroot}/usr/share/package-licenses/syncthing/d6a5f1ecaedd723c325a2063375b3517e808a2b5 || :
cp %{_builddir}/syncthing/vendor/golang.org/x/sys/LICENSE %{buildroot}/usr/share/package-licenses/syncthing/d6a5f1ecaedd723c325a2063375b3517e808a2b5 || :
cp %{_builddir}/syncthing/vendor/golang.org/x/text/LICENSE %{buildroot}/usr/share/package-licenses/syncthing/d6a5f1ecaedd723c325a2063375b3517e808a2b5 || :
cp %{_builddir}/syncthing/vendor/golang.org/x/time/LICENSE %{buildroot}/usr/share/package-licenses/syncthing/d6a5f1ecaedd723c325a2063375b3517e808a2b5 || :
cp %{_builddir}/syncthing/vendor/golang.org/x/tools/LICENSE %{buildroot}/usr/share/package-licenses/syncthing/d6a5f1ecaedd723c325a2063375b3517e808a2b5 || :
cp %{_builddir}/syncthing/vendor/google.golang.org/protobuf/LICENSE %{buildroot}/usr/share/package-licenses/syncthing/74850a25a5319bdddc0d998eb8926c18bada282b || :
pushd ../buildavx2/
install -p -D -m 0755 syncthing -t %{buildroot}/usr/bin/_v3
popd
install -p -D -m 0755 syncthing -t %{buildroot}/usr/bin/
## install_append content

# Install systemd service units
install -p -D -m 0644 etc/linux-systemd/system/*.service -t %{buildroot}/usr/lib/systemd/system/
install -p -D -m 0644 etc/linux-systemd/user/*.service   -t %{buildroot}/usr/lib/systemd/user/

# Install desktop files
install -p -D -m 0644 etc/linux-desktop/*.desktop -t %{buildroot}/usr/share/applications/

# Install sysctl config to improve local LAN sync performance
install -p -D -m 0644 etc/linux-sysctl/*.conf -t %{buildroot}/usr/lib/sysctl.d/

# Install manpages
shopt -s nullglob
for manpage in man/*.[0-9]; do
section=$(expr match "${manpage}" '.*\.\([0-9]\)')
install -p -D -m 0644 ${manpage} -t %{buildroot}/usr/share/man/man${section}/
done
## install_append end
/usr/bin/elf-move.py avx2 %{buildroot}-v3 %{buildroot} %{buildroot}/usr/share/clear/filemap/filemap-%{name}

%files
%defattr(-,root,root,-)

%files bin
%defattr(-,root,root,-)
/usr/bin/_v3/syncthing
/usr/bin/syncthing

%files config
%defattr(-,root,root,-)
/usr/lib/sysctl.d/30-syncthing.conf

%files data
%defattr(-,root,root,-)
/usr/share/applications/syncthing-start.desktop
/usr/share/applications/syncthing-ui.desktop

%files license
%defattr(0644,root,root,0755)
/usr/share/package-licenses/syncthing/039965feff6efd8f281c4d4989a2547a27c9270c
/usr/share/package-licenses/syncthing/06b27345acae9303e13dde9974d2b2e318b05989
/usr/share/package-licenses/syncthing/08021ae73f58f423dd6e7b525e81cf2520f7619e
/usr/share/package-licenses/syncthing/0c40e548c3768125e9fd4c09907b2457341edef6
/usr/share/package-licenses/syncthing/13581bcb019974856e6ab27e6072b7ab22c100db
/usr/share/package-licenses/syncthing/172ca3bbafe312a1cf09cfff26953db2f425c28e
/usr/share/package-licenses/syncthing/174f178b9e4dcfa220b6a12ada1b869e8a6684b1
/usr/share/package-licenses/syncthing/1b2d963c77ddfc6454ca369fc4884e87e256a2e1
/usr/share/package-licenses/syncthing/219c5dccdc6fb5f0e047ca6ce8e0228f12e90017
/usr/share/package-licenses/syncthing/225d7794e5557038980b6f5c898175c1bac63485
/usr/share/package-licenses/syncthing/26bee26046eaa07afedc723e392fcc1341d86739
/usr/share/package-licenses/syncthing/2b8b815229aa8a61e483fb4ba0588b8b6c491890
/usr/share/package-licenses/syncthing/2bb1eaec43fbd55aaffe41c50270b0ec08b68be9
/usr/share/package-licenses/syncthing/3afc456546a3fa3e82c0d21844cd9911d7d4464b
/usr/share/package-licenses/syncthing/3d9ca858ae047e05c8c031e24b41aea21417fc2a
/usr/share/package-licenses/syncthing/41a17a069904e6a10fa1b1bcf67c2e4d836937d1
/usr/share/package-licenses/syncthing/428e62f9df892db59cde7dba84a1f37c49bd4252
/usr/share/package-licenses/syncthing/4539e1c1452683731710f1867fff6d5d148b0c86
/usr/share/package-licenses/syncthing/4b23a2c0bf17e7644903958716e8e01967aa874c
/usr/share/package-licenses/syncthing/535e3badf5b532d842627b504976fbb93bc2d8b8
/usr/share/package-licenses/syncthing/565471fdf06cfb21b7c69c5fc329a1341d5d9ad0
/usr/share/package-licenses/syncthing/59e0fe537bc596157e3417e3ff4038a26f579393
/usr/share/package-licenses/syncthing/5eaad1bc8f139227bee002062efa2e1b603fb2db
/usr/share/package-licenses/syncthing/694bed385b0e246185c61a1d991a7fd92471930b
/usr/share/package-licenses/syncthing/6db801a1f89a986850ad801057410db22a968998
/usr/share/package-licenses/syncthing/736c20a685418b27e6992d88c0959152991d33bf
/usr/share/package-licenses/syncthing/74850a25a5319bdddc0d998eb8926c18bada282b
/usr/share/package-licenses/syncthing/78af3b5baa64be2c32fecd3ef812aee13904da2a
/usr/share/package-licenses/syncthing/78d85619a69f25c64fad9f76fc734a66107b18d4
/usr/share/package-licenses/syncthing/7be82c1a81e7197640a88df91dc82d64b77c7acd
/usr/share/package-licenses/syncthing/7d1bc92f0ee5987fd034a5a8ea664b35236736fc
/usr/share/package-licenses/syncthing/7df059597099bb7dcf25d2a9aedfaf4465f72d8d
/usr/share/package-licenses/syncthing/88b150e4e0f2318a6316840ed631fb2cc62d5fcc
/usr/share/package-licenses/syncthing/90778a2b78620d46a521986f99136e44a1dde89f
/usr/share/package-licenses/syncthing/90857ae97e892cea98fe28613afba3366d56bbf3
/usr/share/package-licenses/syncthing/92170cdc034b2ff819323ff670d3b7266c8bffcd
/usr/share/package-licenses/syncthing/9601f5532b9beb07d32ebf845f3a78f604bf6f27
/usr/share/package-licenses/syncthing/9744cedce099f727b327cd9913a1fdc58a7f5599
/usr/share/package-licenses/syncthing/97c18dd612ad4458f3823e836adb21dd11962ac9
/usr/share/package-licenses/syncthing/9c1bedc0d42f24c24a1bd266f3ce101a4b0579fc
/usr/share/package-licenses/syncthing/9f1b6690bcfc732123ae209c90c62f2ba80dfcb0
/usr/share/package-licenses/syncthing/a0c9c581a56350ef0229f375420d52d8ca68de74
/usr/share/package-licenses/syncthing/a4c50f5c034ae8ad818e6f5773a7d65e03b58b37
/usr/share/package-licenses/syncthing/aab97739ef7d50750adbc9ffbfd1cbf9608eb678
/usr/share/package-licenses/syncthing/b2e4520feb0f9b51ad373256b94c3faf4c1e6871
/usr/share/package-licenses/syncthing/b7a606730713ac061594edab33cf941704b4a95c
/usr/share/package-licenses/syncthing/b7b97d84a5f0b778ab971d2afce44f47c8b6e80a
/usr/share/package-licenses/syncthing/b90cbf29c01e677d454e9aabdc0bd4c0887778c5
/usr/share/package-licenses/syncthing/bf88cc725ad09db6991d26b4af7cc790ef52c6fb
/usr/share/package-licenses/syncthing/c0f4ffe120079028c20033cf13619b9f52434c22
/usr/share/package-licenses/syncthing/c2252212aa407a45427696985f2d8c7f774df3b2
/usr/share/package-licenses/syncthing/d22157abc0fc0b4ae96380c09528e23cf77290a9
/usr/share/package-licenses/syncthing/d6a5f1ecaedd723c325a2063375b3517e808a2b5
/usr/share/package-licenses/syncthing/d78741c6ab8e4933cd2ce6686b234c450f1c3ab5
/usr/share/package-licenses/syncthing/d7e3ed5ac149ac1e2d2e0f4daff081c1dafef1c0
/usr/share/package-licenses/syncthing/da34754c05d40ff81f91de8c1b85ea6e5503e21d
/usr/share/package-licenses/syncthing/e0b06b4bbfdf1ffba0edaaf4aefb22922df8561e
/usr/share/package-licenses/syncthing/e0b761db9d0831cae676bcb303fc7d9095ae9beb
/usr/share/package-licenses/syncthing/e23f0c9f837e16ab8a47710ad840069df16a701b
/usr/share/package-licenses/syncthing/e46e6a6dce75540a865a761f00e65c78b00c5895
/usr/share/package-licenses/syncthing/e9e85ffe1ad083ba47b7c72f5553c3368a655872
/usr/share/package-licenses/syncthing/f4f6a4a62f50348c9f4fa311fd2023d8ed32e380
/usr/share/package-licenses/syncthing/fa644321f4cb0aadb2bd05f398d4a23ae563128b
/usr/share/package-licenses/syncthing/fd6460234f122a19f21affb6d6885269340b9176
/usr/share/package-licenses/syncthing/fe47bb31aed90010edbbd000a09abb9eea90b329

%files man
%defattr(0644,root,root,0755)
/usr/share/man/man1/stdiscosrv.1
/usr/share/man/man1/strelaysrv.1
/usr/share/man/man1/syncthing.1
/usr/share/man/man5/syncthing-config.5
/usr/share/man/man5/syncthing-stignore.5
/usr/share/man/man7/syncthing-bep.7
/usr/share/man/man7/syncthing-device-ids.7
/usr/share/man/man7/syncthing-event-api.7
/usr/share/man/man7/syncthing-faq.7
/usr/share/man/man7/syncthing-globaldisco.7
/usr/share/man/man7/syncthing-localdisco.7
/usr/share/man/man7/syncthing-networking.7
/usr/share/man/man7/syncthing-relay.7
/usr/share/man/man7/syncthing-rest-api.7
/usr/share/man/man7/syncthing-security.7
/usr/share/man/man7/syncthing-versioning.7

%files services
%defattr(-,root,root,-)
/usr/lib/systemd/system/syncthing-resume.service
/usr/lib/systemd/system/syncthing@.service
/usr/lib/systemd/user/syncthing.service
