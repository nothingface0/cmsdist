### RPM external sigcpp 3.0.7
Source: https://github.com/libsigcplusplus/libsigcplusplus/archive/refs/tags/%{realversion}.tar.gz

BuildRequires: autotools

%prep
%setup -q -n libsigc++-%{realversion}
./configure --prefix=%{i} --disable-static

%build
make %{makeprocesses}

%install
make install
# We remove pkg-config files for two reasons:
# * it's actually not required (macosx does not even have it).
# * rpm 4.8 adds a dependency on the system /usr/bin/pkg-config 
#   on linux.
# In the case at some point we build a package that can be build
# only via pkg-config we have to think on how to ship our own
# version.
rm -rf %{i}/lib/pkgconfig
# Read documentation online.
%define drop_files %{i}/share
cp %{i}/lib/sigc++-2.0/include/sigc++config.h %{i}/include/sigc++-2.0/
