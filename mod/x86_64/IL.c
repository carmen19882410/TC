/* Created by Language version: 7.5.0 */
/* NOT VECTORIZED */
#define NRN_VECTORIZED 0
#include <stdio.h>
#include <stdlib.h>
#include <math.h>
#include "scoplib_ansi.h"
#undef PI
#define nil 0
#include "md1redef.h"
#include "section.h"
#include "nrniv_mf.h"
#include "md2redef.h"
 
#if METHOD3
extern int _method3;
#endif

#if !NRNGPU
#undef exp
#define exp hoc_Exp
extern double hoc_Exp(double);
#endif
 
#define nrn_init _nrn_init__kl
#define _nrn_initial _nrn_initial__kl
#define nrn_cur _nrn_cur__kl
#define _nrn_current _nrn_current__kl
#define nrn_jacob _nrn_jacob__kl
#define nrn_state _nrn_state__kl
#define _net_receive _net_receive__kl 
#define rates rates__kl 
#define states states__kl 
 
#define _threadargscomma_ /**/
#define _threadargsprotocomma_ /**/
#define _threadargs_ /**/
#define _threadargsproto_ /**/
 	/*SUPPRESS 761*/
	/*SUPPRESS 762*/
	/*SUPPRESS 763*/
	/*SUPPRESS 765*/
	 extern double *getarg();
 static double *_p; static Datum *_ppvar;
 
#define t nrn_threads->_t
#define dt nrn_threads->_dt
#define gbar _p[0]
#define gka _p[1]
#define n _p[2]
#define l _p[3]
#define ek _p[4]
#define Dn _p[5]
#define Dl _p[6]
#define ik _p[7]
#define _g _p[8]
#define _ion_ek	*_ppvar[0]._pval
#define _ion_ik	*_ppvar[1]._pval
#define _ion_dikdv	*_ppvar[2]._pval
 
#if MAC
#if !defined(v)
#define v _mlhv
#endif
#if !defined(h)
#define h _mlhh
#endif
#endif
 
#if defined(__cplusplus)
extern "C" {
#endif
 static int hoc_nrnpointerindex =  -1;
 /* external NEURON variables */
 extern double celsius;
 /* declaration of user functions */
 static void _hoc_alpl(void);
 static void _hoc_alpn(void);
 static void _hoc_betl(void);
 static void _hoc_betn(void);
 static void _hoc_rates(void);
 static int _mechtype;
extern void _nrn_cacheloop_reg(int, int);
extern void hoc_register_prop_size(int, int, int);
extern void hoc_register_limits(int, HocParmLimits*);
extern void hoc_register_units(int, HocParmUnits*);
extern void nrn_promote(Prop*, int, int);
extern Memb_func* memb_func;
 extern void _nrn_setdata_reg(int, void(*)(Prop*));
 static void _setdata(Prop* _prop) {
 _p = _prop->param; _ppvar = _prop->dparam;
 }
 static void _hoc_setdata() {
 Prop *_prop, *hoc_getdata_range(int);
 _prop = hoc_getdata_range(_mechtype);
   _setdata(_prop);
 hoc_retpushx(1.);
}
 /* connect user functions to hoc names */
 static VoidFunc hoc_intfunc[] = {
 "setdata_kl", _hoc_setdata,
 "alpl_kl", _hoc_alpl,
 "alpn_kl", _hoc_alpn,
 "betl_kl", _hoc_betl,
 "betn_kl", _hoc_betn,
 "rates_kl", _hoc_rates,
 0, 0
};
#define alpl alpl_kl
#define alpn alpn_kl
#define betl betl_kl
#define betn betn_kl
 extern double alpl( double );
 extern double alpn( double );
 extern double betl( double );
 extern double betn( double );
 /* declare global and static user variables */
#define a0n a0n_kl
 double a0n = 0.05;
#define a0l a0l_kl
 double a0l = 0.05;
#define gml gml_kl
 double gml = 1;
#define gmn gmn_kl
 double gmn = 0.55;
#define linf linf_kl
 double linf = 0;
#define lmin lmin_kl
 double lmin = 2;
#define ninf ninf_kl
 double ninf = 0;
#define nmin nmin_kl
 double nmin = 0.1;
#define pw pw_kl
 double pw = -1;
#define qtl qtl_kl
 double qtl = 1;
#define q10 q10_kl
 double q10 = 5;
#define qq qq_kl
 double qq = 5;
#define taun taun_kl
 double taun = 0;
#define taul taul_kl
 double taul = 0;
#define tq tq_kl
 double tq = -40;
#define vhalfl vhalfl_kl
 double vhalfl = -56;
#define vhalfn vhalfn_kl
 double vhalfn = 11;
#define zetal zetal_kl
 double zetal = 3;
#define zetan zetan_kl
 double zetan = -1.5;
 /* some parameters have upper and lower limits */
 static HocParmLimits _hoc_parm_limits[] = {
 0,0,0
};
 static HocParmUnits _hoc_parm_units[] = {
 "vhalfn_kl", "mV",
 "vhalfl_kl", "mV",
 "a0l_kl", "/ms",
 "a0n_kl", "/ms",
 "zetan_kl", "1",
 "zetal_kl", "1",
 "gmn_kl", "1",
 "gml_kl", "1",
 "lmin_kl", "mS",
 "nmin_kl", "mS",
 "pw_kl", "1",
 0,0
};
 static double delta_t = 0.01;
 static double l0 = 0;
 static double n0 = 0;
 static double v = 0;
 /* connect global user variables to hoc */
 static DoubScal hoc_scdoub[] = {
 "vhalfn_kl", &vhalfn_kl,
 "vhalfl_kl", &vhalfl_kl,
 "a0l_kl", &a0l_kl,
 "a0n_kl", &a0n_kl,
 "zetan_kl", &zetan_kl,
 "zetal_kl", &zetal_kl,
 "gmn_kl", &gmn_kl,
 "gml_kl", &gml_kl,
 "lmin_kl", &lmin_kl,
 "nmin_kl", &nmin_kl,
 "pw_kl", &pw_kl,
 "tq_kl", &tq_kl,
 "qq_kl", &qq_kl,
 "q10_kl", &q10_kl,
 "qtl_kl", &qtl_kl,
 "ninf_kl", &ninf_kl,
 "linf_kl", &linf_kl,
 "taul_kl", &taul_kl,
 "taun_kl", &taun_kl,
 0,0
};
 static DoubVec hoc_vdoub[] = {
 0,0,0
};
 static double _sav_indep;
 static void nrn_alloc(Prop*);
static void  nrn_init(_NrnThread*, _Memb_list*, int);
static void nrn_state(_NrnThread*, _Memb_list*, int);
 static void nrn_cur(_NrnThread*, _Memb_list*, int);
static void  nrn_jacob(_NrnThread*, _Memb_list*, int);
 
static int _ode_count(int);
static void _ode_map(int, double**, double**, double*, Datum*, double*, int);
static void _ode_spec(_NrnThread*, _Memb_list*, int);
static void _ode_matsol(_NrnThread*, _Memb_list*, int);
 
#define _cvode_ieq _ppvar[3]._i
 static void _ode_matsol_instance1(_threadargsproto_);
 /* connect range variables in _p that hoc is supposed to know about */
 static const char *_mechanism[] = {
 "7.5.0",
"kl",
 "gbar_kl",
 0,
 "gka_kl",
 0,
 "n_kl",
 "l_kl",
 0,
 0};
 static Symbol* _k_sym;
 
extern Prop* need_memb(Symbol*);

static void nrn_alloc(Prop* _prop) {
	Prop *prop_ion;
	double *_p; Datum *_ppvar;
 	_p = nrn_prop_data_alloc(_mechtype, 9, _prop);
 	/*initialize range parameters*/
 	gbar = 0.01;
 	_prop->param = _p;
 	_prop->param_size = 9;
 	_ppvar = nrn_prop_datum_alloc(_mechtype, 4, _prop);
 	_prop->dparam = _ppvar;
 	/*connect ionic variables to this model*/
 prop_ion = need_memb(_k_sym);
 nrn_promote(prop_ion, 0, 1);
 	_ppvar[0]._pval = &prop_ion->param[0]; /* ek */
 	_ppvar[1]._pval = &prop_ion->param[3]; /* ik */
 	_ppvar[2]._pval = &prop_ion->param[4]; /* _ion_dikdv */
 
}
 static void _initlists();
  /* some states have an absolute tolerance */
 static Symbol** _atollist;
 static HocStateTolerance _hoc_state_tol[] = {
 0,0
};
 static void _update_ion_pointer(Datum*);
 extern Symbol* hoc_lookup(const char*);
extern void _nrn_thread_reg(int, int, void(*)(Datum*));
extern void _nrn_thread_table_reg(int, void(*)(double*, Datum*, Datum*, _NrnThread*, int));
extern void hoc_register_tolerance(int, HocStateTolerance*, Symbol***);
extern void _cvode_abstol( Symbol**, double*, int);

 void _IL_reg() {
	int _vectorized = 0;
  _initlists();
 	ion_reg("k", -10000.);
 	_k_sym = hoc_lookup("k_ion");
 	register_mech(_mechanism, nrn_alloc,nrn_cur, nrn_jacob, nrn_state, nrn_init, hoc_nrnpointerindex, 0);
 _mechtype = nrn_get_mechtype(_mechanism[1]);
     _nrn_setdata_reg(_mechtype, _setdata);
     _nrn_thread_reg(_mechtype, 2, _update_ion_pointer);
  hoc_register_prop_size(_mechtype, 9, 4);
  hoc_register_dparam_semantics(_mechtype, 0, "k_ion");
  hoc_register_dparam_semantics(_mechtype, 1, "k_ion");
  hoc_register_dparam_semantics(_mechtype, 2, "k_ion");
  hoc_register_dparam_semantics(_mechtype, 3, "cvodeieq");
 	hoc_register_cvode(_mechtype, _ode_count, _ode_map, _ode_spec, _ode_matsol);
 	hoc_register_tolerance(_mechtype, _hoc_state_tol, &_atollist);
 	hoc_register_var(hoc_scdoub, hoc_vdoub, hoc_intfunc);
 	ivoc_help("help ?1 kl /home/ocnc/Desktop/Thalamic_neuron_model/mod/x86_64/IL.mod\n");
 hoc_register_limits(_mechtype, _hoc_parm_limits);
 hoc_register_units(_mechtype, _hoc_parm_units);
 }
static int _reset;
static char *modelname = "K-A channel from Klee Ficker and Heinemann";

static int error;
static int _ninits = 0;
static int _match_recurse=1;
static void _modl_cleanup(){ _match_recurse=1;}
static int rates(double);
 
static int _ode_spec1(_threadargsproto_);
/*static int _ode_matsol1(_threadargsproto_);*/
 static int _slist1[2], _dlist1[2];
 static int states(_threadargsproto_);
 
double alpn (  double _lv ) {
   double _lalpn;
 double _lzeta ;
 _lzeta = zetan + pw / ( 1.0 + exp ( ( _lv - tq ) / qq ) ) ;
   _lalpn = exp ( 1.e-3 * _lzeta * ( _lv - vhalfn ) * 9.648e4 / ( 8.315 * ( 273.16 + celsius ) ) ) ;
   
return _lalpn;
 }
 
static void _hoc_alpn(void) {
  double _r;
   _r =  alpn (  *getarg(1) );
 hoc_retpushx(_r);
}
 
double betn (  double _lv ) {
   double _lbetn;
 double _lzeta ;
 _lzeta = zetan + pw / ( 1.0 + exp ( ( _lv - tq ) / qq ) ) ;
   _lbetn = exp ( 1.e-3 * _lzeta * gmn * ( _lv - vhalfn ) * 9.648e4 / ( 8.315 * ( 273.16 + celsius ) ) ) ;
   
return _lbetn;
 }
 
static void _hoc_betn(void) {
  double _r;
   _r =  betn (  *getarg(1) );
 hoc_retpushx(_r);
}
 
double alpl (  double _lv ) {
   double _lalpl;
 _lalpl = exp ( 1.e-3 * zetal * ( _lv - vhalfl ) * 9.648e4 / ( 8.315 * ( 273.16 + celsius ) ) ) ;
   
return _lalpl;
 }
 
static void _hoc_alpl(void) {
  double _r;
   _r =  alpl (  *getarg(1) );
 hoc_retpushx(_r);
}
 
double betl (  double _lv ) {
   double _lbetl;
 _lbetl = exp ( 1.e-3 * zetal * gml * ( _lv - vhalfl ) * 9.648e4 / ( 8.315 * ( 273.16 + celsius ) ) ) ;
   
return _lbetl;
 }
 
static void _hoc_betl(void) {
  double _r;
   _r =  betl (  *getarg(1) );
 hoc_retpushx(_r);
}
 
/*CVODE*/
 static int _ode_spec1 () {_reset=0;
 {
   rates ( _threadargscomma_ v ) ;
   Dn = ( ninf - n ) / taun ;
   Dl = ( linf - l ) / taul ;
   }
 return _reset;
}
 static int _ode_matsol1 () {
 rates ( _threadargscomma_ v ) ;
 Dn = Dn  / (1. - dt*( ( ( ( - 1.0 ) ) ) / taun )) ;
 Dl = Dl  / (1. - dt*( ( ( ( - 1.0 ) ) ) / taul )) ;
  return 0;
}
 /*END CVODE*/
 static int states () {_reset=0;
 {
   rates ( _threadargscomma_ v ) ;
    n = n + (1. - exp(dt*(( ( ( - 1.0 ) ) ) / taun)))*(- ( ( ( ninf ) ) / taun ) / ( ( ( ( - 1.0 ) ) ) / taun ) - n) ;
    l = l + (1. - exp(dt*(( ( ( - 1.0 ) ) ) / taul)))*(- ( ( ( linf ) ) / taul ) / ( ( ( ( - 1.0 ) ) ) / taul ) - l) ;
   }
  return 0;
}
 
static int  rates (  double _lv ) {
   double _la , _lqt ;
 _lqt = pow( q10 , ( ( celsius - 24.0 ) / 10.0 ) ) ;
   _la = alpn ( _threadargscomma_ _lv ) ;
   taun = betn ( _threadargscomma_ _lv ) / ( _lqt * a0n * ( 1.0 + _la ) ) ;
   if ( taun < nmin ) {
     taun = nmin ;
     }
   ninf = 1.0 / ( 1.0 + exp ( - ( _lv + 60.0 ) / 20.0 ) ) ;
   taul = 0.26 * ( _lv + 50.0 ) / qtl * 20.0 ;
   if ( taul < lmin / qtl ) {
     taul = lmin / qtl ;
     }
   linf = 1.0 / ( 1.0 + exp ( ( _lv + 30.0 ) / 20.0 ) ) ;
    return 0; }
 
static void _hoc_rates(void) {
  double _r;
   _r = 1.;
 rates (  *getarg(1) );
 hoc_retpushx(_r);
}
 
static int _ode_count(int _type){ return 2;}
 
static void _ode_spec(_NrnThread* _nt, _Memb_list* _ml, int _type) {
   Datum* _thread;
   Node* _nd; double _v; int _iml, _cntml;
  _cntml = _ml->_nodecount;
  _thread = _ml->_thread;
  for (_iml = 0; _iml < _cntml; ++_iml) {
    _p = _ml->_data[_iml]; _ppvar = _ml->_pdata[_iml];
    _nd = _ml->_nodelist[_iml];
    v = NODEV(_nd);
  ek = _ion_ek;
     _ode_spec1 ();
  }}
 
static void _ode_map(int _ieq, double** _pv, double** _pvdot, double* _pp, Datum* _ppd, double* _atol, int _type) { 
 	int _i; _p = _pp; _ppvar = _ppd;
	_cvode_ieq = _ieq;
	for (_i=0; _i < 2; ++_i) {
		_pv[_i] = _pp + _slist1[_i];  _pvdot[_i] = _pp + _dlist1[_i];
		_cvode_abstol(_atollist, _atol, _i);
	}
 }
 
static void _ode_matsol_instance1(_threadargsproto_) {
 _ode_matsol1 ();
 }
 
static void _ode_matsol(_NrnThread* _nt, _Memb_list* _ml, int _type) {
   Datum* _thread;
   Node* _nd; double _v; int _iml, _cntml;
  _cntml = _ml->_nodecount;
  _thread = _ml->_thread;
  for (_iml = 0; _iml < _cntml; ++_iml) {
    _p = _ml->_data[_iml]; _ppvar = _ml->_pdata[_iml];
    _nd = _ml->_nodelist[_iml];
    v = NODEV(_nd);
  ek = _ion_ek;
 _ode_matsol_instance1(_threadargs_);
 }}
 extern void nrn_update_ion_pointer(Symbol*, Datum*, int, int);
 static void _update_ion_pointer(Datum* _ppvar) {
   nrn_update_ion_pointer(_k_sym, _ppvar, 0, 0);
   nrn_update_ion_pointer(_k_sym, _ppvar, 1, 3);
   nrn_update_ion_pointer(_k_sym, _ppvar, 2, 4);
 }

static void initmodel() {
  int _i; double _save;_ninits++;
 _save = t;
 t = 0.0;
{
  l = l0;
  n = n0;
 {
   rates ( _threadargscomma_ v ) ;
   n = ninf ;
   l = linf ;
   }
  _sav_indep = t; t = _save;

}
}

static void nrn_init(_NrnThread* _nt, _Memb_list* _ml, int _type){
Node *_nd; double _v; int* _ni; int _iml, _cntml;
#if CACHEVEC
    _ni = _ml->_nodeindices;
#endif
_cntml = _ml->_nodecount;
for (_iml = 0; _iml < _cntml; ++_iml) {
 _p = _ml->_data[_iml]; _ppvar = _ml->_pdata[_iml];
#if CACHEVEC
  if (use_cachevec) {
    _v = VEC_V(_ni[_iml]);
  }else
#endif
  {
    _nd = _ml->_nodelist[_iml];
    _v = NODEV(_nd);
  }
 v = _v;
  ek = _ion_ek;
 initmodel();
 }}

static double _nrn_current(double _v){double _current=0.;v=_v;{ {
   gka = gbar * n * l ;
   ik = gka * ( v - ek ) ;
   }
 _current += ik;

} return _current;
}

static void nrn_cur(_NrnThread* _nt, _Memb_list* _ml, int _type){
Node *_nd; int* _ni; double _rhs, _v; int _iml, _cntml;
#if CACHEVEC
    _ni = _ml->_nodeindices;
#endif
_cntml = _ml->_nodecount;
for (_iml = 0; _iml < _cntml; ++_iml) {
 _p = _ml->_data[_iml]; _ppvar = _ml->_pdata[_iml];
#if CACHEVEC
  if (use_cachevec) {
    _v = VEC_V(_ni[_iml]);
  }else
#endif
  {
    _nd = _ml->_nodelist[_iml];
    _v = NODEV(_nd);
  }
  ek = _ion_ek;
 _g = _nrn_current(_v + .001);
 	{ double _dik;
  _dik = ik;
 _rhs = _nrn_current(_v);
  _ion_dikdv += (_dik - ik)/.001 ;
 	}
 _g = (_g - _rhs)/.001;
  _ion_ik += ik ;
#if CACHEVEC
  if (use_cachevec) {
	VEC_RHS(_ni[_iml]) -= _rhs;
  }else
#endif
  {
	NODERHS(_nd) -= _rhs;
  }
 
}}

static void nrn_jacob(_NrnThread* _nt, _Memb_list* _ml, int _type){
Node *_nd; int* _ni; int _iml, _cntml;
#if CACHEVEC
    _ni = _ml->_nodeindices;
#endif
_cntml = _ml->_nodecount;
for (_iml = 0; _iml < _cntml; ++_iml) {
 _p = _ml->_data[_iml];
#if CACHEVEC
  if (use_cachevec) {
	VEC_D(_ni[_iml]) += _g;
  }else
#endif
  {
     _nd = _ml->_nodelist[_iml];
	NODED(_nd) += _g;
  }
 
}}

static void nrn_state(_NrnThread* _nt, _Memb_list* _ml, int _type){
Node *_nd; double _v = 0.0; int* _ni; int _iml, _cntml;
#if CACHEVEC
    _ni = _ml->_nodeindices;
#endif
_cntml = _ml->_nodecount;
for (_iml = 0; _iml < _cntml; ++_iml) {
 _p = _ml->_data[_iml]; _ppvar = _ml->_pdata[_iml];
 _nd = _ml->_nodelist[_iml];
#if CACHEVEC
  if (use_cachevec) {
    _v = VEC_V(_ni[_iml]);
  }else
#endif
  {
    _nd = _ml->_nodelist[_iml];
    _v = NODEV(_nd);
  }
 v=_v;
{
  ek = _ion_ek;
 { error =  states();
 if(error){fprintf(stderr,"at line 72 in file IL.mod:\n	SOLVE states METHOD cnexp\n"); nrn_complain(_p); abort_run(error);}
 } }}

}

static void terminal(){}

static void _initlists() {
 int _i; static int _first = 1;
  if (!_first) return;
 _slist1[0] = &(n) - _p;  _dlist1[0] = &(Dn) - _p;
 _slist1[1] = &(l) - _p;  _dlist1[1] = &(Dl) - _p;
_first = 0;
}
