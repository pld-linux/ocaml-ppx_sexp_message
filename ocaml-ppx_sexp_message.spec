#
# Conditional build:
%bcond_without	ocaml_opt	# native optimized binaries (bytecode is always built)

# not yet available on x32 (ocaml 4.02.1), update when upstream will support it
%ifnarch %{ix86} %{x8664} %{arm} aarch64 ppc sparc sparcv9
%undefine	with_ocaml_opt
%endif

Summary:	A ppx rewriter for easy construction of S-expressions
Summary(pl.UTF-8):	Moduł przepisujący ppx do łatwego konstruowania S-wyrażeń
Name:		ocaml-ppx_sexp_message
Version:	0.14.1
Release:	1
License:	MIT
Group:		Libraries
#Source0Download: https://github.com/janestreet/ppx_sexp_message/tags
Source0:	https://github.com/janestreet/ppx_sexp_message/archive/v%{version}/ppx_sexp_message-%{version}.tar.gz
# Source0-md5:	a6f4478ba28e7f16cd37789e64a7cb79
URL:		https://github.com/janestreet/ppx_sexp_message
BuildRequires:	ocaml >= 1:4.04.2
BuildRequires:	ocaml-base-devel >= 0.14
BuildRequires:	ocaml-base-devel < 0.15
BuildRequires:	ocaml-dune >= 2.0.0
BuildRequires:	ocaml-ppx_here-devel >= 0.14
BuildRequires:	ocaml-ppx_here-devel < 0.15
BuildRequires:	ocaml-ppx_sexp_conv-devel >= 0.14
BuildRequires:	ocaml-ppx_sexp_conv-devel < 0.15
BuildRequires:	ocaml-ppxlib-devel >= 0.18.0
%requires_eq	ocaml-runtime
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define		debug_package	%{nil}

%description
The aim of ppx_sexp_message is to ease the creation of S-expressions
in OCaml. This is mainly motivated by writing error and debugging
messages, where one needs to construct a S-expression based on various
element of the context such as function arguments.

This package contains files needed to run bytecode executables using
ppx_sexp_message library.

%description -l pl.UTF-8
Celem ppx_sexp_message jest ułatwienie tworzenia S-wyrażeń w OCamlu.
Motywacją do tego jest głównie wypisywanie komunikatów o błędach i
diagnostycznych, gdzie potrzeba skonstruować S-wyrażenia w oparciu o
różne elementy kontekstu, takie jak argumenty funkcji.

Pakiet ten zawiera binaria potrzebne do uruchamiania programów
używających biblioteki ppx_sexp_message.

%package devel
Summary:	A ppx rewriter for easy construction of S-expressions - development part
Summary(pl.UTF-8):	Moduł przepisujący ppx do łatwego konstruowania S-wyrażeń - część programistyczna
Group:		Development/Libraries
Requires:	%{name} = %{version}-%{release}
%requires_eq	ocaml
Requires:	ocaml-base-devel >= 0.14
Requires:	ocaml-ppx_here-devel >= 0.14
Requires:	ocaml-ppx_sexp_conv-devel >= 0.14
Requires:	ocaml-ppxlib-devel >= 0.18.0

%description devel
This package contains files needed to develop OCaml programs using
ppx_sexp_message library.

%description devel -l pl.UTF-8
Pakiet ten zawiera pliki niezbędne do tworzenia programów w OCamlu
używających biblioteki ppx_sexp_message.

%prep
%setup -q -n ppx_sexp_message-%{version}

%build
dune build --verbose

%install
rm -rf $RPM_BUILD_ROOT

dune install --destdir=$RPM_BUILD_ROOT

# sources
%{__rm} $RPM_BUILD_ROOT%{_libdir}/ocaml/ppx_sexp_message/*.ml
%{__rm} $RPM_BUILD_ROOT%{_libdir}/ocaml/ppx_sexp_message/*/*.ml
# packaged as %doc
%{__rm} -r $RPM_BUILD_ROOT%{_prefix}/doc/ppx_sexp_message

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc CHANGES.md LICENSE.md README.md
%dir %{_libdir}/ocaml/ppx_sexp_message
%attr(755,root,root) %{_libdir}/ocaml/ppx_sexp_message/ppx.exe
%{_libdir}/ocaml/ppx_sexp_message/META
%{_libdir}/ocaml/ppx_sexp_message/*.cma
%dir %{_libdir}/ocaml/ppx_sexp_message/expander
%{_libdir}/ocaml/ppx_sexp_message/expander/*.cma
%if %{with ocaml_opt}
%attr(755,root,root) %{_libdir}/ocaml/ppx_sexp_message/*.cmxs
%attr(755,root,root) %{_libdir}/ocaml/ppx_sexp_message/expander/*.cmxs
%endif

%files devel
%defattr(644,root,root,755)
%{_libdir}/ocaml/ppx_sexp_message/*.cmi
%{_libdir}/ocaml/ppx_sexp_message/*.cmt
%{_libdir}/ocaml/ppx_sexp_message/*.cmti
%{_libdir}/ocaml/ppx_sexp_message/*.mli
%{_libdir}/ocaml/ppx_sexp_message/expander/*.cmi
%{_libdir}/ocaml/ppx_sexp_message/expander/*.cmt
%{_libdir}/ocaml/ppx_sexp_message/expander/*.cmti
%{_libdir}/ocaml/ppx_sexp_message/expander/*.mli
%if %{with ocaml_opt}
%{_libdir}/ocaml/ppx_sexp_message/ppx_sexp_message.a
%{_libdir}/ocaml/ppx_sexp_message/*.cmx
%{_libdir}/ocaml/ppx_sexp_message/*.cmxa
%{_libdir}/ocaml/ppx_sexp_message/expander/ppx_sexp_message_expander.a
%{_libdir}/ocaml/ppx_sexp_message/expander/*.cmx
%{_libdir}/ocaml/ppx_sexp_message/expander/*.cmxa
%endif
%{_libdir}/ocaml/ppx_sexp_message/dune-package
%{_libdir}/ocaml/ppx_sexp_message/opam
