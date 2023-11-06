### RPM external eigen aa6964bf3a34fd607837dd8123bc42465185c4f8
## INITENV +PATH PKG_CONFIG_PATH %{i}/share/pkgconfig
## NOCOMPILER
## INCLUDE cpp-standard
%define tag d288717d64d507efc32ea784d072e4825f431bec
%define branch cms/master/%{realversion}
%define github_user cms-externals
Source: git+https://github.com/%{github_user}/eigen-git-mirror.git?obj=%{branch}/%{tag}&export=%{n}-%{realversion}&output=/%{n}-%{realversion}-%{tag}.tgz
BuildRequires: cmake

%prep
%setup -n %{n}-%{realversion}

%build
mkdir build
cd build
cmake -DCMAKE_INSTALL_PREFIX=%{i} -DBUILD_TESTING=OFF -DCMAKE_CXX_STANDARD=%{cms_cxx_standard} ../

%install
cd build
make install

%post
%{relocateConfig}share/pkgconfig/eigen3.pc
