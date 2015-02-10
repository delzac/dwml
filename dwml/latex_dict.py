# -*- coding: utf-8 -*-

"""
Thinks for
http://web.ift.uib.no/Teori/KURS/WRK/TeX/symALL.html
http://en.wikibooks.org/wiki/LaTeX/Mathematics
http://www.ctan.org/tex-archive/macros/latex/contrib/unicode-math
https://github.com/wspr/unicode-math/blob/master/unicode-math-table.tex
"""

CHR = {
	#Unicode : Latex Math Symbols
	#Top accents
	'\u0300' : r'\grave{{{0}}}',
	'\u0301' : r'\acute{{{0}}}',
	'\u0302' : r'\hat{{{0}}}',
	'\u0303' : r'\tilde{{{0}}}',  
	'\u0304' : r'\bar{{{0}}}',
	'\u0305' : r'\overbar{{{0}}}',
	'\u0306' : r'\breve{{{0}}}',
	'\u0307' : r'\dot{{{0}}}',	  
	'\u0308' : r'\ddot{{{0}}}',
	'\u0309' : r'\ovhook{{{0}}}',
	'\u030A' : r'\ocirc{{{0}}}}',
	'\u030C' : r'\check{{{0}}}}',
	'\u0310' : r'\candra{{{0}}}',
	'\u0312' : r'\oturnedcomma{{{0}}}',
	'\u0315' : r'\ocommatopright{{{0}}}',
	'\u031A' : r'\droang{{{0}}}',
	'\u0338' : r'\not{{{0}}}',
	'\u20D0' : r'\leftharpoonaccent{{{0}}}',
	'\u20D1' : r'\rightharpoonaccent{{{0}}}',
	'\u20D2' : r'\vertoverlay{{{0}}}',
	'\u20D6' : r'\overleftarrow{{{0}}}',
	'\u20D7' : r'\vec{{{0}}}',
	'\u20DB' : r'\dddot{{{0}}}',
	'\u20DC' : r'\ddddot{{{0}}}',
	'\u20E1' : r'\overleftrightarrow{{{0}}}',
	'\u20E7' : r'\annuity{{{0}}}',
	'\u20E9' : r'\widebridgeabove{{{0}}}',
	'\u20F0' : r'\asteraccent{{{0}}}',
	 #Bottom accents
	'\u0330' : r'\wideutilde{{{0}}}',
	'\u0331' : r'\underbar{{{0}}}',
	'\u20E8' : r'\threeunderdot{{{0}}}',
	'\u20EC' : r'\underrightharpoondown{{{0}}}',
	'\u20ED' : r'\underleftharpoondown{{{0}}}',
	'\u20EE' : r'\underledtarrow{{{0}}}',
	'\u20EF' : r'\underrightarrow{{{0}}}',
}

T = {
	'\u2192' : r'\rightarrow',
	#Greek letters
	'\U0001D6FC' : r'\alpha',
	'\U0001D6FD' : r'\beta',
	'\U0001D6FE' : r'\gamma',
	'\U0001D6FF' : r'\theta',
	'\U0001D700' : r'\epsilon',
	'\U0001D701' : r'\zeta',
	'\U0001D702' : r'\eta',
	'\U0001D703' : r'\theta',
	'\U0001D704' : r'\iota',
	'\U0001D705' : r'\kappa',
	'\U0001D706' : r'\lambda',
	'\U0001D707' : r'\mu',
	'\U0001D708' : r'\nu',
	'\U0001D709' : r'\xi',
	'\U0001D70A' : r'\omicron',
	'\U0001D70B' : r'\pi',
	'\U0001D70C' : r'\rho',
	'\U0001D70D' : r'\varsigma',
	'\U0001D70E' : r'\sigma',
	'\U0001D70F' : r'\tau',
	'\U0001D710' : r'\upsilon',
	'\U0001D711' : r'\phi',
	'\U0001D712' : r'\chi',
	'\U0001D713' : r'\psi',
	'\U0001D714' : r'\omega',
	'\U0001D715' : r'\partial',
	'\U0001D716' : r'\varepsilon',
	'\U0001D717' : r'\vartheta',
	'\U0001D718' : r'\varkappa',
	'\U0001D719' : r'\varphi',
	'\U0001D71A' : r'\varrho',
	'\U0001D71B' : r'\varpi', 
}

CHR_DEFAULT = {
	'ACC_VAL':r'\hat{{{0}}}',
}

POS = {
	'top' : r'\overline{{{0}}}', # not sure
	'bot' : r'\underline{{{0}}}',
}

POS_DEFAULT = {
	'BAR_VAL': r'\overline{{{0}}}',
}

SUB = '_{{{0}}}'

SUP = '^{{{0}}}'

F  = r'\frac{{{num}}}{{{den}}}'