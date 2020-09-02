
機器學習的數學基礎
------------------

[TOC]

### 高等數學

**1.導數定義：**

導數和微分的概念

$f'({{x}_{0}})=\underset{\Delta x\to 0}{\mathop{\lim }}\,\frac{f({{x}_{0}}+\Delta x)-f({{x}_{0}})}{\Delta x}$    （1）

或者：

$f'({{x}_{0}})=\underset{x\to {{x}_{0}}}{\mathop{\lim }}\,\frac{f(x)-f({{x}_{0}})}{x-{{x}_{0}}}$           （2）

**2.左右導數導數的幾何意義和物理意義**

函數$f(x)$在$x_0$處的左、右導數分別定義為：

左導數：${{{f}'}_{-}}({{x}_{0}})=\underset{\Delta x\to {{0}^{-}}}{\mathop{\lim }}\,\frac{f({{x}_{0}}+\Delta x)-f({{x}_{0}})}{\Delta x}=\underset{x\to x_{0}^{-}}{\mathop{\lim }}\,\frac{f(x)-f({{x}_{0}})}{x-{{x}_{0}}},(x={{x}_{0}}+\Delta x)$

右導數：${{{f}'}_{+}}({{x}_{0}})=\underset{\Delta x\to {{0}^{+}}}{\mathop{\lim }}\,\frac{f({{x}_{0}}+\Delta x)-f({{x}_{0}})}{\Delta x}=\underset{x\to x_{0}^{+}}{\mathop{\lim }}\,\frac{f(x)-f({{x}_{0}})}{x-{{x}_{0}}}$

**3.函數的可導性與連續性之間的關係**

**Th1:** 函數$f(x)$在$x_0$處可微$\Leftrightarrow f(x)$在$x_0$處可導

**Th2:** 若函數在點$x_0$處可導，則$y=f(x)$在點$x_0$處連續，反之則不成立。即函數連續不一定可導。

**Th3:** ${f}'({{x}_{0}})$存在$\Leftrightarrow {{{f}'}_{-}}({{x}_{0}})={{{f}'}_{+}}({{x}_{0}})$

**4.平面曲線的切線和法線**

切線方程 : $y-{{y}_{0}}=f'({{x}_{0}})(x-{{x}_{0}})$
法線方程：$y-{{y}_{0}}=-\frac{1}{f'({{x}_{0}})}(x-{{x}_{0}}),f'({{x}_{0}})\ne 0$

**5.四則運算法則**
設函數$u=u(x)，v=v(x)$]在點$x$可導則
(1) $(u\pm v{)}'={u}'\pm {v}'$       $d(u\pm v)=du\pm dv$
(2)$(uv{)}'=u{v}'+v{u}'$        $d(uv)=udv+vdu$
(3) $(\frac{u}{v}{)}'=\frac{v{u}'-u{v}'}{{{v}^{2}}}(v\ne 0)$       $d(\frac{u}{v})=\frac{vdu-udv}{{{v}^{2}}}$

**6.基本導數與微分表**
(1) $y=c​$（常數）       ${y}'=0​$          $dy=0​$
(2) $y={{x}^{\alpha }}​$($\alpha ​$為實數)    ${y}'=\alpha {{x}^{\alpha -1}}​$      $dy=\alpha {{x}^{\alpha -1}}dx​$
(3) $y={{a}^{x}}​$      ${y}'={{a}^{x}}\ln a​$         $dy={{a}^{x}}\ln adx​$
  特例:   $({{{e}}^{x}}{)}'={{{e}}^{x}}​$             $d({{{e}}^{x}})={{{e}}^{x}}dx​$

(4) $y={{\log }_{a}}x$   ${y}'=\frac{1}{x\ln a}$           

$dy=\frac{1}{x\ln a}dx$
  特例:$y=\ln x$                      $(\ln x{)}'=\frac{1}{x}$       $d(\ln x)=\frac{1}{x}dx$

(5) $y=\sin x$         

${y}'=\cos x$        $d(\sin x)=\cos xdx$

(6) $y=\cos x$      

${y}'=-\sin x$       $d(\cos x)=-\sin xdx$

(7) $y=\tan x$  

${y}'=\frac{1}{{{\cos }^{2}}x}={{\sec }^{2}}x$  $d(\tan x)={{\sec }^{2}}xdx$
(8) $y=\cot x$ ${y}'=-\frac{1}{{{\sin }^{2}}x}=-{{\csc }^{2}}x$  $d(\cot x)=-{{\csc }^{2}}xdx$
(9) $y=\sec x$ ${y}'=\sec x\tan x$     

 $d(\sec x)=\sec x\tan xdx$
(10) $y=\csc x$ ${y}'=-\csc x\cot x$    

$d(\csc x)=-\csc x\cot xdx$
(11) $y=\arcsin x$  

${y}'=\frac{1}{\sqrt{1-{{x}^{2}}}}$   

$d(\arcsin x)=\frac{1}{\sqrt{1-{{x}^{2}}}}dx$
(12) $y=\arccos x$ 

${y}'=-\frac{1}{\sqrt{1-{{x}^{2}}}}$     $d(\arccos x)=-\frac{1}{\sqrt{1-{{x}^{2}}}}dx$

(13) $y=\arctan x$ 

${y}'=\frac{1}{1+{{x}^{2}}}$     $d(\arctan x)=\frac{1}{1+{{x}^{2}}}dx$

(14) $y=\operatorname{arc}\cot x$      

${y}'=-\frac{1}{1+{{x}^{2}}}$   

$d(\operatorname{arc}\cot x)=-\frac{1}{1+{{x}^{2}}}dx$
(15) $y=shx$    

${y}'=chx$       $d(shx)=chxdx$

(16) $y=chx$    

${y}'=shx$       $d(chx)=shxdx$

**7.複合函數，反函數，隱函數以及參數方程所確定的函數的微分法**

(1) 反函數的運算法則: 設$y=f(x)$在點$x$的某鄰域內單調連續，在點$x$處可導且${f}'(x)\ne 0$，則其反函數在點$x$所對應的$y$處可導，並且有$\frac{dy}{dx}=\frac{1}{\frac{dx}{dy}}$
(2) 複合函數的運算法則:若$\mu =\varphi (x)$在點$x$可導,而$y=f(\mu )$在對應點$\mu $($\mu =\varphi (x)$)可導,則複合函數$y=f(\varphi (x))$在點$x$可導,且${y}'={f}'(\mu )\cdot {\varphi }'(x)$
(3) 隱函數導數$\frac{dy}{dx}$的求法一般有三種方法：
1)方程兩邊對$x$求導，要記住$y$是$x$的函數，則$y$的函數是$x$的複合函數.例如$\frac{1}{y}$，${{y}^{2}}$，$ln y$，${{{e}}^{y}}$等均是$x$的複合函數.
對$x$求導應按複合函數連鎖法則做.
2)公式法.由$F(x,y)=0$知 $\frac{dy}{dx}=-\frac{{{{{F}'}}_{x}}(x,y)}{{{{{F}'}}_{y}}(x,y)}$,其中，${{{F}'}_{x}}(x,y)$，
${{{F}'}_{y}}(x,y)$分別表示$F(x,y)$對$x$和$y$的偏導數
3)利用微分形式不變性

**8.常用高階導數公式**

（1）$({{a}^{x}}){{\,}^{(n)}}={{a}^{x}}{{\ln }^{n}}a\quad (a>{0})\quad \quad ({{{e}}^{x}}){{\,}^{(n)}}={e}{{\,}^{x}}$
（2）$(\sin kx{)}{{\,}^{(n)}}={{k}^{n}}\sin (kx+n\cdot \frac{\pi }{{2}})$
（3）$(\cos kx{)}{{\,}^{(n)}}={{k}^{n}}\cos (kx+n\cdot \frac{\pi }{{2}})$
（4）$({{x}^{m}}){{\,}^{(n)}}=m(m-1)\cdots (m-n+1){{x}^{m-n}}$
（5）$(\ln x){{\,}^{(n)}}={{(-{1})}^{(n-{1})}}\frac{(n-{1})!}{{{x}^{n}}}$
（6）萊布尼茲公式：若$u(x)\,,v(x)$均$n$階可導，則
 ${{(uv)}^{(n)}}=\sum\limits_{i={0}}^{n}{c_{n}^{i}{{u}^{(i)}}{{v}^{(n-i)}}}$，其中${{u}^{({0})}}=u$，${{v}^{({0})}}=v$

**9.微分中值定理，泰勒公式**

**Th1:**(費馬定理)

若函數$f(x)$滿足條件：
(1)函數$f(x)$在${{x}_{0}}$的某鄰域內有定義，並且在此鄰域內恆有
$f(x)\le f({{x}_{0}})$或$f(x)\ge f({{x}_{0}})$,

(2) $f(x)$在${{x}_{0}}$處可導,則有 ${f}'({{x}_{0}})=0$

**Th2:**(羅爾定理) 

設函數$f(x)$滿足條件：
(1)在閉區間$[a,b]$上連續；

(2)在$(a,b)$內可導；

(3)$f(a)=f(b)$；

則在$(a,b)$內一存在個$\xi $，使  ${f}'(\xi )=0$
**Th3:** (拉格朗日中值定理) 

設函數$f(x)$滿足條件：
(1)在$[a,b]$上連續；

(2)在$(a,b)$內可導；

則在$(a,b)$內一存在個$\xi $，使  $\frac{f(b)-f(a)}{b-a}={f}'(\xi )$

**Th4:** (柯西中值定理)

 設函數$f(x)$，$g(x)$滿足條件：
(1) 在$[a,b]$上連續；

(2) 在$(a,b)$內可導且${f}'(x)$，${g}'(x)$均存在，且${g}'(x)\ne 0$

則在$(a,b)$內存在一個$\xi $，使  $\frac{f(b)-f(a)}{g(b)-g(a)}=\frac{{f}'(\xi )}{{g}'(\xi )}$

**10.洛必達法則**
法則Ⅰ ($\frac{0}{0}$型)
設函數$f\left( x \right),g\left( x \right)$滿足條件：
 $\underset{x\to {{x}_{0}}}{\mathop{\lim }}\,f\left( x \right)=0,\underset{x\to {{x}_{0}}}{\mathop{\lim }}\,g\left( x \right)=0$; 

$f\left( x \right),g\left( x \right)$在${{x}_{0}}$的鄰域內可導，(在${{x}_{0}}$處可除外)且${g}'\left( x \right)\ne 0$;

$\underset{x\to {{x}_{0}}}{\mathop{\lim }}\,\frac{{f}'\left( x \right)}{{g}'\left( x \right)}$存在(或$\infty $)。

則:
$\underset{x\to {{x}_{0}}}{\mathop{\lim }}\,\frac{f\left( x \right)}{g\left( x \right)}=\underset{x\to {{x}_{0}}}{\mathop{\lim }}\,\frac{{f}'\left( x \right)}{{g}'\left( x \right)}$。
法則${{I}'}$ ($\frac{0}{0}$型)設函數$f\left( x \right),g\left( x \right)$滿足條件：
$\underset{x\to \infty }{\mathop{\lim }}\,f\left( x \right)=0,\underset{x\to \infty }{\mathop{\lim }}\,g\left( x \right)=0$;

存在一個$X>0$,當$\left| x \right|>X$時,$f\left( x \right),g\left( x \right)$可導,且${g}'\left( x \right)\ne 0$;$\underset{x\to {{x}_{0}}}{\mathop{\lim }}\,\frac{{f}'\left( x \right)}{{g}'\left( x \right)}$存在(或$\infty $)。

則:
$\underset{x\to {{x}_{0}}}{\mathop{\lim }}\,\frac{f\left( x \right)}{g\left( x \right)}=\underset{x\to {{x}_{0}}}{\mathop{\lim }}\,\frac{{f}'\left( x \right)}{{g}'\left( x \right)}$
法則Ⅱ($\frac{\infty }{\infty }$型) 設函數$f\left( x \right),g\left( x \right)$滿足條件：
$\underset{x\to {{x}_{0}}}{\mathop{\lim }}\,f\left( x \right)=\infty ,\underset{x\to {{x}_{0}}}{\mathop{\lim }}\,g\left( x \right)=\infty $;   $f\left( x \right),g\left( x \right)$在${{x}_{0}}$ 的鄰域內可導(在${{x}_{0}}$處可除外)且${g}'\left( x \right)\ne 0$;$\underset{x\to {{x}_{0}}}{\mathop{\lim }}\,\frac{{f}'\left( x \right)}{{g}'\left( x \right)}$存在(或$\infty $)。則
$\underset{x\to {{x}_{0}}}{\mathop{\lim }}\,\frac{f\left( x \right)}{g\left( x \right)}=\underset{x\to {{x}_{0}}}{\mathop{\lim }}\,\frac{{f}'\left( x \right)}{{g}'\left( x \right)}.$同理法則${I{I}'}$($\frac{\infty }{\infty }$型)仿法則${{I}'}$可寫出。

**11.泰勒公式**

設函數$f(x)$在點${{x}_{0}}$處的某鄰域內具有$n+1$階導數，則對該鄰域內異於${{x}_{0}}$的任意點$x$，在${{x}_{0}}$與$x$之間至少存在
一個$\xi $，使得：
$f(x)=f({{x}_{0}})+{f}'({{x}_{0}})(x-{{x}_{0}})+\frac{1}{2!}{f}''({{x}_{0}}){{(x-{{x}_{0}})}^{2}}+\cdots $ 
$+\frac{{{f}^{(n)}}({{x}_{0}})}{n!}{{(x-{{x}_{0}})}^{n}}+{{R}_{n}}(x)$
 其中 ${{R}_{n}}(x)=\frac{{{f}^{(n+1)}}(\xi )}{(n+1)!}{{(x-{{x}_{0}})}^{n+1}}$稱為$f(x)$在點${{x}_{0}}$處的$n$階泰勒餘項。

令${{x}_{0}}=0$，則$n$階泰勒公式
$f(x)=f(0)+{f}'(0)x+\frac{1}{2!}{f}''(0){{x}^{2}}+\cdots +\frac{{{f}^{(n)}}(0)}{n!}{{x}^{n}}+{{R}_{n}}(x)$……(1)
其中 ${{R}_{n}}(x)=\frac{{{f}^{(n+1)}}(\xi )}{(n+1)!}{{x}^{n+1}}$，$\xi $在0與$x$之間.(1)式稱為麥克勞林公式

**常用五種函數在${{x}_{0}}=0$處的泰勒公式**

(1) ${{{e}}^{x}}=1+x+\frac{1}{2!}{{x}^{2}}+\cdots +\frac{1}{n!}{{x}^{n}}+\frac{{{x}^{n+1}}}{(n+1)!}{{e}^{\xi }}$ 

或 $=1+x+\frac{1}{2!}{{x}^{2}}+\cdots +\frac{1}{n!}{{x}^{n}}+o({{x}^{n}})$

(2) $\sin x=x-\frac{1}{3!}{{x}^{3}}+\cdots +\frac{{{x}^{n}}}{n!}\sin \frac{n\pi }{2}+\frac{{{x}^{n+1}}}{(n+1)!}\sin (\xi +\frac{n+1}{2}\pi )$

或  $=x-\frac{1}{3!}{{x}^{3}}+\cdots +\frac{{{x}^{n}}}{n!}\sin \frac{n\pi }{2}+o({{x}^{n}})$

(3) $\cos x=1-\frac{1}{2!}{{x}^{2}}+\cdots +\frac{{{x}^{n}}}{n!}\cos \frac{n\pi }{2}+\frac{{{x}^{n+1}}}{(n+1)!}\cos (\xi +\frac{n+1}{2}\pi )$

或   $=1-\frac{1}{2!}{{x}^{2}}+\cdots +\frac{{{x}^{n}}}{n!}\cos \frac{n\pi }{2}+o({{x}^{n}})$

(4) $\ln (1+x)=x-\frac{1}{2}{{x}^{2}}+\frac{1}{3}{{x}^{3}}-\cdots +{{(-1)}^{n-1}}\frac{{{x}^{n}}}{n}+\frac{{{(-1)}^{n}}{{x}^{n+1}}}{(n+1){{(1+\xi )}^{n+1}}}$

或      $=x-\frac{1}{2}{{x}^{2}}+\frac{1}{3}{{x}^{3}}-\cdots +{{(-1)}^{n-1}}\frac{{{x}^{n}}}{n}+o({{x}^{n}})$

(5) ${{(1+x)}^{m}}=1+mx+\frac{m(m-1)}{2!}{{x}^{2}}+\cdots +\frac{m(m-1)\cdots (m-n+1)}{n!}{{x}^{n}}$ 
$+\frac{m(m-1)\cdots (m-n+1)}{(n+1)!}{{x}^{n+1}}{{(1+\xi )}^{m-n-1}}$ 

或 ${{(1+x)}^{m}}=1+mx+\frac{m(m-1)}{2!}{{x}^{2}}+\cdots $ $+\frac{m(m-1)\cdots (m-n+1)}{n!}{{x}^{n}}+o({{x}^{n}})$

**12.函數單調性的判斷**
**Th1:**  設函數$f(x)$在$(a,b)$區間內可導，如果對$\forall x\in (a,b)$，都有$f\,'(x)>0$（或$f\,'(x)<0$），則函數$f(x)$在$(a,b)$內是單調增加的（或單調減少）

**Th2:** （取極值的必要條件）設函數$f(x)$在${{x}_{0}}$處可導，且在${{x}_{0}}$處取極值，則$f\,'({{x}_{0}})=0$。

**Th3:** （取極值的第一充分條件）設函數$f(x)$在${{x}_{0}}$的某一鄰域內可微，且$f\,'({{x}_{0}})=0$（或$f(x)$在${{x}_{0}}$處連續，但$f\,'({{x}_{0}})$不存在。）
(1)若當$x$經過${{x}_{0}}$時，$f\,'(x)$由“+”變“-”，則$f({{x}_{0}})$為極大值；
(2)若當$x​$經過${{x}_{0}}​$時，$f\,'(x)$由“-”變“+”，則$f({{x}_{0}})$為極小值；
(3)若$f\,'(x)$經過$x={{x}_{0}}$的兩側不變號，則$f({{x}_{0}})$不是極值。

**Th4:** (取極值的第二充分條件)設$f(x)$在點${{x}_{0}}$處有$f''(x)\ne 0$，且$f\,'({{x}_{0}})=0$，則 當$f'\,'({{x}_{0}})<0$時，$f({{x}_{0}})$為極大值；
當$f'\,'({{x}_{0}})>0$時，$f({{x}_{0}})$為極小值。
註：如果$f'\,'({{x}_{0}})<0$，此方法失效。

**13.漸近線的求法**
(1)水平漸近線   若$\underset{x\to +\infty }{\mathop{\lim }}\,f(x)=b$，或$\underset{x\to -\infty }{\mathop{\lim }}\,f(x)=b$，則

$y=b$稱為函數$y=f(x)$的水準漸近線。

(2)鉛直漸近線   若$\underset{x\to x_{0}^{-}}{\mathop{\lim }}\,f(x)=\infty $，或$\underset{x\to x_{0}^{+}}{\mathop{\lim }}\,f(x)=\infty $，則

$x={{x}_{0}}$稱為$y=f(x)$的鉛直漸近線。

(3)斜漸近線   若$a=\underset{x\to \infty }{\mathop{\lim }}\,\frac{f(x)}{x},\quad b=\underset{x\to \infty }{\mathop{\lim }}\,[f(x)-ax]$，則
$y=ax+b$稱為$y=f(x)$的斜漸近線。

**14.函數凹凸性的判斷**
**Th1:** (凹凸性的判別定理）若在I上$f''(x)<0$（或$f''(x)>0$），則$f(x)$在I上是凸的（或凹的）。

**Th2:** (拐點的判別定理1)若在${{x}_{0}}$處$f''(x)=0$，（或$f''(x)$不存在），當$x$變動經過${{x}_{0}}$時，$f''(x)$變號，則$({{x}_{0}},f({{x}_{0}}))$為拐點。

**Th3:** (拐點的判別定理2)設$f(x)$在${{x}_{0}}$點的某鄰域內有三階導數，且$f''(x)=0$，$f'''(x)\ne 0$，則$({{x}_{0}},f({{x}_{0}}))$為拐點。

**15.弧微分**

$dS=\sqrt{1+y{{'}^{2}}}dx$

**16.曲率**

曲線$y=f(x)$在點$(x,y)$處的曲率$k=\frac{\left| y'' \right|}{{{(1+y{{'}^{2}})}^{\tfrac{3}{2}}}}$。
對於參數方程$\left\{ \begin{align}  & x=\varphi (t) \\  & y=\psi (t) \\ \end{align} \right.,$$k=\frac{\left| \varphi '(t)\psi ''(t)-\varphi ''(t)\psi '(t) \right|}{{{[\varphi {{'}^{2}}(t)+\psi {{'}^{2}}(t)]}^{\tfrac{3}{2}}}}$。

**17.曲率半徑**

曲線在點$M$處的曲率$k(k\ne 0)$與曲線在點$M$處的曲率半徑$\rho $有如下關係：$\rho =\frac{1}{k}$。

### 線性代數

#### 行列式

**1.行列式按行（列）展開定理**

(1) 設$A = ( a_{{ij}} )_{n \times n}$，則：$a_{i1}A_{j1} +a_{i2}A_{j2} + \cdots + a_{{in}}A_{{jn}} = \begin{cases}|A|,i=j\\ 0,i \neq j\end{cases}$


或$a_{1i}A_{1j} + a_{2i}A_{2j} + \cdots + a_{{ni}}A_{{nj}} = \begin{cases}|A|,i=j\\ 0,i \neq j\end{cases}$即 $AA^{*} = A^{*}A = \left| A \right|E,$其中：$A^{*} = \begin{pmatrix} A_{11} & A_{12} & \ldots & A_{1n} \\ A_{21} & A_{22} & \ldots & A_{2n} \\ \ldots & \ldots & \ldots & \ldots \\ A_{n1} & A_{n2} & \ldots & A_{{nn}} \\ \end{pmatrix} = (A_{{ji}}) = {(A_{{ij}})}^{T}$

$D_{n} = \begin{vmatrix} 1 & 1 & \ldots & 1 \\ x_{1} & x_{2} & \ldots & x_{n} \\ \ldots & \ldots & \ldots & \ldots \\ x_{1}^{n - 1} & x_{2}^{n - 1} & \ldots & x_{n}^{n - 1} \\ \end{vmatrix} = \prod_{1 \leq j < i \leq n}^{}\,(x_{i} - x_{j})$

(2) 設$A,B$為$n$階方陣，則$\left| {AB} \right| = \left| A \right|\left| B \right| = \left| B \right|\left| A \right| = \left| {BA} \right|$，但$\left| A \pm B \right| = \left| A \right| \pm \left| B \right|$不一定成立。

(3) $\left| {kA} \right| = k^{n}\left| A \right|$,$A$為$n$階方陣。

(4) 設$A$為$n$階方陣，$|A^{T}| = |A|;|A^{- 1}| = |A|^{- 1}$（若$A$可逆），$|A^{*}| = |A|^{n - 1}$

$n \geq 2$

(5) $\left| \begin{matrix}  & {A\quad O} \\  & {O\quad B} \\ \end{matrix} \right| = \left| \begin{matrix}  & {A\quad C} \\  & {O\quad B} \\ \end{matrix} \right| = \left| \begin{matrix}  & {A\quad O} \\  & {C\quad B} \\ \end{matrix} \right| =| A||B|$
，$A,B$為方陣，但$\left| \begin{matrix} {O} & A_{m \times m} \\  B_{n \times n} & { O} \\ \end{matrix} \right| = ({- 1)}^{{mn}}|A||B|$ 。

(6) 范德蒙行列式$D_{n} = \begin{vmatrix} 1 & 1 & \ldots & 1 \\ x_{1} & x_{2} & \ldots & x_{n} \\ \ldots & \ldots & \ldots & \ldots \\ x_{1}^{n - 1} & x_{2}^{n 1} & \ldots & x_{n}^{n - 1} \\ \end{vmatrix} =  \prod_{1 \leq j < i \leq n}^{}\,(x_{i} - x_{j})$

設$A$是$n$階方陣，$\lambda_{i}(i = 1,2\cdots,n)$是$A$的$n$個特徵值，則
$|A| = \prod_{i = 1}^{n}\lambda_{i}​$

#### 矩陣

矩陣：$m \times n$個數$a_{{ij}}$排成$m$行$n$列的表格$\begin{bmatrix}  a_{11}\quad a_{12}\quad\cdots\quad a_{1n} \\ a_{21}\quad a_{22}\quad\cdots\quad a_{2n} \\ \quad\cdots\cdots\cdots\cdots\cdots \\  a_{m1}\quad a_{m2}\quad\cdots\quad a_{{mn}} \\ \end{bmatrix}$ 稱為矩陣，簡記為$A$，或者$\left( a_{{ij}} \right)_{m \times n}$ 。若$m = n$，則稱$A$是$n$階矩陣或$n$階方陣。

**矩陣的線性運算**

**1.矩陣的加法**

設$A = (a_{{ij}}),B = (b_{{ij}})$是兩個$m \times n$矩陣，則$m \times n$ 矩陣$C = c_{{ij}}) = a_{{ij}} + b_{{ij}}$稱為矩陣$A$與$B$的和，記為$A + B = C$ 。

**2.矩陣的數乘**

設$A = (a_{{ij}})$是$m \times n$矩陣，$k$是一個常數，則$m \times n$矩陣$(ka_{{ij}})$稱為數$k$與矩陣$A$的數乘，記為${kA}$。

**3.矩陣的乘法**

設$A = (a_{{ij}})$是$m \times n$矩陣，$B = (b_{{ij}})$是$n \times s$矩陣，那麼$m \times s$矩陣$C = (c_{{ij}})$，其中$c_{{ij}} = a_{i1}b_{1j} + a_{i2}b_{2j} + \cdots + a_{{in}}b_{{nj}} = \sum_{k =1}^{n}{a_{{ik}}b_{{kj}}}$稱為${AB}$的乘積，記為$C = AB$ 。

**4.** $\mathbf{A}^{\mathbf{T}}$**、**$\mathbf{A}^{\mathbf{-1}}$**、**$\mathbf{A}^{\mathbf{*}}$**三者之間的關係**

(1) ${(A^{T})}^{T} = A,{(AB)}^{T} = B^{T}A^{T},{(kA)}^{T} = kA^{T},{(A \pm B)}^{T} = A^{T} \pm B^{T}$

(2) $\left( A^{- 1} \right)^{- 1} = A,\left( {AB} \right)^{- 1} = B^{- 1}A^{- 1},\left( {kA} \right)^{- 1} = \frac{1}{k}A^{- 1},$

但 ${(A \pm B)}^{- 1} = A^{- 1} \pm B^{- 1}$不一定成立。

(3) $\left( A^{*} \right)^{*} = |A|^{n - 2}\ A\ \ (n \geq 3)$，$\left({AB} \right)^{*} = B^{*}A^{*},$ $\left( {kA} \right)^{*} = k^{n -1}A^{*}{\ \ }\left( n \geq 2 \right)$

但$\left( A \pm B \right)^{*} = A^{*} \pm B^{*}$不一定成立。

(4) ${(A^{- 1})}^{T} = {(A^{T})}^{- 1},\ \left( A^{- 1} \right)^{*} ={(AA^{*})}^{- 1},{(A^{*})}^{T} = \left( A^{T} \right)^{*}$

**5.有關**$\mathbf{A}^{\mathbf{*}}$**的結論**

(1) $AA^{*} = A^{*}A = |A|E$

(2) $|A^{*}| = |A|^{n - 1}\ (n \geq 2),\ \ \ \ {(kA)}^{*} = k^{n -1}A^{*},{{\ \ }\left( A^{*} \right)}^{*} = |A|^{n - 2}A(n \geq 3)$

(3) 若$A$可逆，則$A^{*} = |A|A^{- 1},{(A^{*})}^{*} = \frac{1}{|A|}A$

(4) 若$A​$為$n​$階方陣，則：

$r(A^*)=\begin{cases}n,\quad r(A)=n\\ 1,\quad r(A)=n-1\\ 0,\quad r(A)<n-1\end{cases}$

**6.有關**$\mathbf{A}^{\mathbf{- 1}}$**的結論**

$A$可逆$\Leftrightarrow AB = E; \Leftrightarrow |A| \neq 0; \Leftrightarrow r(A) = n;$

$\Leftrightarrow A$可以表示為初等矩陣的乘積；$\Leftrightarrow A;\Leftrightarrow Ax = 0$。

**7.有關矩陣秩的結論**

(1) 秩$r(A)$=行秩=列秩；

(2) $r(A_{m \times n}) \leq \min(m,n);$

(3) $A \neq 0 \Rightarrow r(A) \geq 1$；

(4) $r(A \pm B) \leq r(A) + r(B);$

(5) 初等變換不改變矩陣的秩

(6) $r(A) + r(B) - n \leq r(AB) \leq \min(r(A),r(B)),$特別若$AB = O$
則：$r(A) + r(B) \leq n$

(7) 若$A^{- 1}$存在$\Rightarrow r(AB) = r(B);$ 若$B^{- 1}$存在
$\Rightarrow r(AB) = r(A);$

若$r(A_{m \times n}) = n \Rightarrow r(AB) = r(B);$ 若$r(A_{m \times s}) = n\Rightarrow r(AB) = r\left( A \right)$。

(8) $r(A_{m \times s}) = n \Leftrightarrow Ax = 0$只有零解

**8.分塊求逆公式**

$\begin{pmatrix} A & O \\ O & B \\ \end{pmatrix}^{- 1} = \begin{pmatrix} A^{-1} & O \\ O & B^{- 1} \\ \end{pmatrix}$； $\begin{pmatrix} A & C \\ O & B \\\end{pmatrix}^{- 1} = \begin{pmatrix} A^{- 1}& - A^{- 1}CB^{- 1} \\ O & B^{- 1} \\ \end{pmatrix}$；

$\begin{pmatrix} A & O \\ C & B \\ \end{pmatrix}^{- 1} = \begin{pmatrix}  A^{- 1}&{O} \\   - B^{- 1}CA^{- 1} & B^{- 1} \\\end{pmatrix}$； $\begin{pmatrix} O & A \\ B & O \\ \end{pmatrix}^{- 1} =\begin{pmatrix} O & B^{- 1} \\ A^{- 1} & O \\ \end{pmatrix}$

這裡$A$，$B$均為可逆方陣。

#### 向量

**1.有關向量組的線性表示**

(1)$\alpha_{1},\alpha_{2},\cdots,\alpha_{s}$線性相關$\Leftrightarrow$至少有一個向量可以用其餘向量線性表示。

(2)$\alpha_{1},\alpha_{2},\cdots,\alpha_{s}$線性無關，$\alpha_{1},\alpha_{2},\cdots,\alpha_{s}$，$\beta$線性相關$\Leftrightarrow \beta$可以由$\alpha_{1},\alpha_{2},\cdots,\alpha_{s}$唯一線性表示。

(3) $\beta$可以由$\alpha_{1},\alpha_{2},\cdots,\alpha_{s}$線性表示
$\Leftrightarrow r(\alpha_{1},\alpha_{2},\cdots,\alpha_{s}) =r(\alpha_{1},\alpha_{2},\cdots,\alpha_{s},\beta)$ 。

**2.有關向量組的線性相關性**

(1)部分相關，整體相關；整體無關，部分無關.

(2) ① $n$個$n$維向量
$\alpha_{1},\alpha_{2}\cdots\alpha_{n}$線性無關$\Leftrightarrow \left|\left\lbrack \alpha_{1}\alpha_{2}\cdots\alpha_{n} \right\rbrack \right| \neq0$， $n$個$n$維向量$\alpha_{1},\alpha_{2}\cdots\alpha_{n}$線性相關
$\Leftrightarrow |\lbrack\alpha_{1},\alpha_{2},\cdots,\alpha_{n}\rbrack| = 0$
。

② $n + 1$個$n$維向量線性相關。

③ 若$\alpha_{1},\alpha_{2}\cdots\alpha_{S}$線性無關，則添加分量後仍線性無關；或一組向量線性相關，去掉某些分量後仍線性相關。

**3.有關向量組的線性表示**

(1) $\alpha_{1},\alpha_{2},\cdots,\alpha_{s}$線性相關$\Leftrightarrow$至少有一個向量可以用其餘向量線性表示。

(2) $\alpha_{1},\alpha_{2},\cdots,\alpha_{s}$線性無關，$\alpha_{1},\alpha_{2},\cdots,\alpha_{s}$，$\beta$線性相關$\Leftrightarrow\beta$ 可以由$\alpha_{1},\alpha_{2},\cdots,\alpha_{s}$唯一線性表示。

(3) $\beta$可以由$\alpha_{1},\alpha_{2},\cdots,\alpha_{s}$線性表示
$\Leftrightarrow r(\alpha_{1},\alpha_{2},\cdots,\alpha_{s}) =r(\alpha_{1},\alpha_{2},\cdots,\alpha_{s},\beta)$

**4.向量組的秩與矩陣的秩之間的關係**

設$r(A_{m \times n}) =r$，則$A$的秩$r(A)$與$A$的行列向量組的線性相關性關係為：

(1) 若$r(A_{m \times n}) = r = m$，則$A$的行向量組線性無關。

(2) 若$r(A_{m \times n}) = r < m$，則$A$的行向量組線性相關。

(3) 若$r(A_{m \times n}) = r = n$，則$A$的列向量組線性無關。

(4) 若$r(A_{m \times n}) = r < n$，則$A$的列向量組線性相關。

**5.**$\mathbf{n}$**維向量空間的基變換公式及過渡矩陣**

若$\alpha_{1},\alpha_{2},\cdots,\alpha_{n}$與$\beta_{1},\beta_{2},\cdots,\beta_{n}$是向量空間$V$的兩組基，則基變換公式為：

$(\beta_{1},\beta_{2},\cdots,\beta_{n}) = (\alpha_{1},\alpha_{2},\cdots,\alpha_{n})\begin{bmatrix}  c_{11}& c_{12}& \cdots & c_{1n} \\  c_{21}& c_{22}&\cdots & c_{2n} \\ \cdots & \cdots & \cdots & \cdots \\  c_{n1}& c_{n2} & \cdots & c_{{nn}} \\\end{bmatrix} = (\alpha_{1},\alpha_{2},\cdots,\alpha_{n})C$

其中$C$是可逆矩陣，稱為由基$\alpha_{1},\alpha_{2},\cdots,\alpha_{n}$到基$\beta_{1},\beta_{2},\cdots,\beta_{n}$的過渡矩陣。

**6.坐標變換公式**

若向量$\gamma$在基$\alpha_{1},\alpha_{2},\cdots,\alpha_{n}$與基$\beta_{1},\beta_{2},\cdots,\beta_{n}$的坐標分別是
$X = {(x_{1},x_{2},\cdots,x_{n})}^{T}$，

$Y = \left( y_{1},y_{2},\cdots,y_{n} \right)^{T}$ 即： $\gamma =x_{1}\alpha_{1} + x_{2}\alpha_{2} + \cdots + x_{n}\alpha_{n} = y_{1}\beta_{1} +y_{2}\beta_{2} + \cdots + y_{n}\beta_{n}$，則向量坐標變換公式為$X = CY$ 或$Y = C^{- 1}X$，其中$C$是從基$\alpha_{1},\alpha_{2},\cdots,\alpha_{n}$到基$\beta_{1},\beta_{2},\cdots,\beta_{n}$的過渡矩陣。

**7.向量的內積**

$(\alpha,\beta) = a_{1}b_{1} + a_{2}b_{2} + \cdots + a_{n}b_{n} = \alpha^{T}\beta = \beta^{T}\alpha$

**8.Schmidt正交化**

若$\alpha_{1},\alpha_{2},\cdots,\alpha_{s}$線性無關，則可構造$\beta_{1},\beta_{2},\cdots,\beta_{s}$使其兩兩正交，且$\beta_{i}$僅是$\alpha_{1},\alpha_{2},\cdots,\alpha_{i}$的線性組合$(i= 1,2,\cdots,n)$，再把$\beta_{i}$單位化，記$\gamma_{i} =\frac{\beta_{i}}{\left| \beta_{i}\right|}$，則$\gamma_{1},\gamma_{2},\cdots,\gamma_{i}$是規範正交向量組。其中
$\beta_{1} = \alpha_{1}$， $\beta_{2} = \alpha_{2} -\frac{(\alpha_{2},\beta_{1})}{(\beta_{1},\beta_{1})}\beta_{1}$ ， $\beta_{3} =\alpha_{3} - \frac{(\alpha_{3},\beta_{1})}{(\beta_{1},\beta_{1})}\beta_{1} -\frac{(\alpha_{3},\beta_{2})}{(\beta_{2},\beta_{2})}\beta_{2}$ ，

............

$\beta_{s} = \alpha_{s} - \frac{(\alpha_{s},\beta_{1})}{(\beta_{1},\beta_{1})}\beta_{1} - \frac{(\alpha_{s},\beta_{2})}{(\beta_{2},\beta_{2})}\beta_{2} - \cdots - \frac{(\alpha_{s},\beta_{s - 1})}{(\beta_{s - 1},\beta_{s - 1})}\beta_{s - 1}$

**9.正交基及規範正交基**

向量空間一組基中的向量如果兩兩正交，就稱為正交基；若正交基中每個向量都是單位向量，就稱其為規範正交基。

#### 線性方程組

**1．克萊姆法則**

線性方程組$\begin{cases}  a_{11}x_{1} + a_{12}x_{2} + \cdots +a_{1n}x_{n} = b_{1} \\   a_{21}x_{1} + a_{22}x_{2} + \cdots + a_{2n}x_{n} =b_{2} \\   \quad\cdots\cdots\cdots\cdots\cdots\cdots\cdots\cdots\cdots \\ a_{n1}x_{1} + a_{n2}x_{2} + \cdots + a_{{nn}}x_{n} = b_{n} \\ \end{cases}$，如果係數行列式$D = \left| A \right| \neq 0$，則方程組有唯一解，$x_{1} = \frac{D_{1}}{D},x_{2} = \frac{D_{2}}{D},\cdots,x_{n} =\frac{D_{n}}{D}$，其中$D_{j}$是把$D$中第$j$列元素換成方程組右端的常數列所得的行列式。

**2.** $n$階矩陣$A$可逆$\Leftrightarrow Ax = 0$只有零解。$\Leftrightarrow\forall b,Ax = b$總有唯一解，一般地，$r(A_{m \times n}) = n \Leftrightarrow Ax= 0$只有零解。

**3.非奇次線性方程組有解的充分必要條件，線性方程組解的性質和解的結構**

(1) 設$A$為$m \times n$矩陣，若$r(A_{m \times n}) = m$，則對$Ax =b$而言必有$r(A) = r(A \vdots b) = m$，從而$Ax = b$有解。

(2) 設$x_{1},x_{2},\cdots x_{s}$為$Ax = b$的解，則$k_{1}x_{1} + k_{2}x_{2}\cdots + k_{s}x_{s}$當$k_{1} + k_{2} + \cdots + k_{s} = 1$時仍為$Ax =b$的解；但當$k_{1} + k_{2} + \cdots + k_{s} = 0$時，則為$Ax =0$的解。特別$\frac{x_{1} + x_{2}}{2}$為$Ax = b$的解；$2x_{3} - (x_{1} +x_{2})$為$Ax = 0$的解。

(3) 非齊次線性方程組${Ax} = b$無解$\Leftrightarrow r(A) + 1 =r(\overline{A}) \Leftrightarrow b$不能由$A$的列向量$\alpha_{1},\alpha_{2},\cdots,\alpha_{n}$線性表示。

**4.奇次線性方程組的基礎解系和通解，解空間，非奇次線性方程組的通解**

(1) 齊次方程組${Ax} = 0$恆有解(必有零解)。當有非零解時，由於解向量的任意線性組合仍是該齊次方程組的解向量，因此${Ax}= 0$的全體解向量構成一個向量空間，稱為該方程組的解空間，解空間的維數是$n - r(A)$，解空間的一組基稱為齊次方程組的基礎解系。

(2) $\eta_{1},\eta_{2},\cdots,\eta_{t}$是${Ax} = 0$的基礎解系，即：

1) $\eta_{1},\eta_{2},\cdots,\eta_{t}$是${Ax} = 0$的解；

2) $\eta_{1},\eta_{2},\cdots,\eta_{t}$線性無關；

3) ${Ax} = 0$的任一解都可以由$\eta_{1},\eta_{2},\cdots,\eta_{t}$線性表出.
$k_{1}\eta_{1} + k_{2}\eta_{2} + \cdots + k_{t}\eta_{t}$是${Ax} = 0$的通解，其中$k_{1},k_{2},\cdots,k_{t}$是任意常數。

#### 矩陣的特徵值和特徵向量

**1.矩陣的特徵值和特徵向量的概念及性質**

(1) 設$\lambda$是$A$的一個特徵值，則 ${kA},{aA} + {bE},A^{2},A^{m},f(A),A^{T},A^{- 1},A^{*}$有一個特徵值分別為
${kλ},{aλ} + b,\lambda^{2},\lambda^{m},f(\lambda),\lambda,\lambda^{- 1},\frac{|A|}{\lambda},$且對應特徵向量相同（$A^{T}$ 例外）。

(2)若$\lambda_{1},\lambda_{2},\cdots,\lambda_{n}$為$A$的$n$個特徵值，則$\sum_{i= 1}^{n}\lambda_{i} = \sum_{i = 1}^{n}a_{{ii}},\prod_{i = 1}^{n}\lambda_{i}= |A|$ ,從而$|A| \neq 0 \Leftrightarrow A$沒有特徵值。

(3)設$\lambda_{1},\lambda_{2},\cdots,\lambda_{s}$為$A$的$s$個特徵值，對應特徵向量為$\alpha_{1},\alpha_{2},\cdots,\alpha_{s}$，

若: $\alpha = k_{1}\alpha_{1} + k_{2}\alpha_{2} + \cdots + k_{s}\alpha_{s}$ ,

則: $A^{n}\alpha = k_{1}A^{n}\alpha_{1} + k_{2}A^{n}\alpha_{2} + \cdots +k_{s}A^{n}\alpha_{s} = k_{1}\lambda_{1}^{n}\alpha_{1} +k_{2}\lambda_{2}^{n}\alpha_{2} + \cdots k_{s}\lambda_{s}^{n}\alpha_{s}$ 。

**2.相似變換、相似矩陣的概念及性質**

(1) 若$A \sim B$，則

1) $A^{T} \sim B^{T},A^{- 1} \sim B^{- 1},,A^{*} \sim B^{*}$

2) $|A| = |B|,\sum_{i = 1}^{n}A_{{ii}} = \sum_{i =1}^{n}b_{{ii}},r(A) = r(B)$

3) $|\lambda E - A| = |\lambda E - B|$，對$\forall\lambda$成立

**3.矩陣可相似對角化的充分必要條件**

(1)設$A$為$n$階方陣，則$A$可對角化$\Leftrightarrow$對每個$k_{i}$重根特徵值$\lambda_{i}$，有$n-r(\lambda_{i}E - A) = k_{i}$

(2) 設$A$可對角化，則由$P^{- 1}{AP} = \Lambda,$有$A = {PΛ}P^{-1}$，從而$A^{n} = P\Lambda^{n}P^{- 1}$

(3) 重要結論

1) 若$A \sim B,C \sim D​$，則$\begin{bmatrix}  A & O \\ O & C \\\end{bmatrix} \sim \begin{bmatrix} B & O \\  O & D \\\end{bmatrix}​$.

2) 若$A \sim B$，則$f(A) \sim f(B),\left| f(A) \right| \sim \left| f(B)\right|$，其中$f(A)$為關於$n$階方陣$A$的多項式。

3) 若$A$為可對角化矩陣，則其非零特徵值的個數(重根重複計算)＝秩($A$)

**4.實對稱矩陣的特徵值、特徵向量及相似對角陣**

(1)相似矩陣：設$A,B$為兩個$n$階方陣，如果存在一個可逆矩陣$P$，使得$B =P^{- 1}{AP}$成立，則稱矩陣$A$與$B$相似，記為$A \sim B$。

(2)相似矩陣的性質：如果$A \sim B$則有：

1) $A^{T} \sim B^{T}$

2) $A^{- 1} \sim B^{- 1}$ （若$A$，$B$均可逆）

3) $A^{k} \sim B^{k}$ （$k$為正整數）

4) $\left| {λE} - A \right| = \left| {λE} - B \right|$，從而$A,B$
有相同的特徵值

5) $\left| A \right| = \left| B \right|$，從而$A,B$同時可逆或者不可逆

6) 秩$\left( A \right) =$秩$\left( B \right),\left| {λE} - A \right| =\left| {λE} - B \right|$，$A,B$不一定相似

#### 二次型

**1.**$\mathbf{n}$**個變數**$\mathbf{x}_{\mathbf{1}}\mathbf{,}\mathbf{x}_{\mathbf{2}}\mathbf{,\cdots,}\mathbf{x}_{\mathbf{n}}$**的二次齊次函數**

$f(x_{1},x_{2},\cdots,x_{n}) = \sum_{i = 1}^{n}{\sum_{j =1}^{n}{a_{{ij}}x_{i}y_{j}}}$，其中$a_{{ij}} = a_{{ji}}(i,j =1,2,\cdots,n)$，稱為$n$元二次型，簡稱二次型. 若令$x = \ \begin{bmatrix}x_{1} \\ x_{1} \\  \vdots \\ x_{n} \\ \end{bmatrix},A = \begin{bmatrix}  a_{11}& a_{12}& \cdots & a_{1n} \\  a_{21}& a_{22}& \cdots & a_{2n} \\ \cdots &\cdots &\cdots &\cdots \\  a_{n1}& a_{n2} & \cdots & a_{{nn}} \\\end{bmatrix}$,這二次型$f$可改寫成矩陣向量形式$f =x^{T}{Ax}$。其中$A$稱為二次型矩陣，因為$a_{{ij}} =a_{{ji}}(i,j =1,2,\cdots,n)$，所以二次型矩陣均為對稱矩陣，且二次型與對稱矩陣一一對應，並把矩陣$A$的秩稱為二次型的秩。

**2.慣性定理，二次型的標準形和規範形**

(1) 慣性定理

對於任一二次型，不論選取怎樣的契約變換使它化為僅含平方項的標準型，其正負慣性指數與所選變換無關，這就是所謂的慣性定理。

(2) 標準形

二次型$f = \left( x_{1},x_{2},\cdots,x_{n} \right) =x^{T}{Ax}$經過契約變換$x = {Cy}$化為$f = x^{T}{Ax} =y^{T}C^{T}{AC}$

$y = \sum_{i = 1}^{r}{d_{i}y_{i}^{2}}$稱為 $f(r \leq n)$的標準形。在一般的數域內，二次型的標準形不是唯一的，與所作的契約變換有關，但係數不為零的平方項的個數由$r(A)$唯一確定。

(3) 規範形

任一實二次型$f$都可經過契約變換化為規範形$f = z_{1}^{2} + z_{2}^{2} + \cdots z_{p}^{2} - z_{p + 1}^{2} - \cdots -z_{r}^{2}$，其中$r$為$A$的秩，$p$為正慣性指數，$r -p$為負慣性指數，且規範型唯一。

**3.用正交變換和配方法化二次型為標準形，二次型及其矩陣的正定性**

設$A$正定$\Rightarrow {kA}(k > 0),A^{T},A^{- 1},A^{*}$正定；$|A| >0$,$A$可逆；$a_{{ii}} > 0$，且$|A_{{ii}}| > 0$

$A$，$B$正定$\Rightarrow A +B$正定，但${AB}$，${BA}$不一定正定

$A$正定$\Leftrightarrow f(x) = x^{T}{Ax} > 0,\forall x \neq 0$

$\Leftrightarrow A$的各階順序主子式全大於零

$\Leftrightarrow A$的所有特徵值大於零

$\Leftrightarrow A$的正慣性指數為$n$

$\Leftrightarrow$存在可逆陣$P$使$A = P^{T}P$

$\Leftrightarrow$存在正交矩陣$Q$，使$Q^{T}{AQ} = Q^{- 1}{AQ} =\begin{pmatrix} \lambda_{1} & & \\ \begin{matrix}  & \\  & \\ \end{matrix} &\ddots & \\  & & \lambda_{n} \\ \end{pmatrix},$

其中$\lambda_{i} > 0,i = 1,2,\cdots,n.$正定$\Rightarrow {kA}(k >0),A^{T},A^{- 1},A^{*}$正定； $|A| > 0,A$可逆；$a_{{ii}} >0$，且$|A_{{ii}}| > 0$ 。

### 機率論和數理統計

#### 隨機事件和機率

**1.事件的關係與運算**

(1) 子事件：$A \subset B$，若$A$發生，則$B$發生。

(2) 相等事件：$A = B$，即$A \subset B$，且$B \subset A$ 。

(3) 和事件：$A\bigcup B$（或$A + B$），$A$與$B$中至少有一個發生。

(4) 差事件：$A - B$，$A$發生但$B$不發生。

(5) 積事件：$A\bigcap B$（或${AB}$），$A$與$B$同時發生。

(6) 互斥事件（互不相容）：$A\bigcap B$=$\varnothing$。

(7) 互逆事件（對立事件）：
$A\bigcap B=\varnothing ,A\bigcup B=\Omega ,A=\bar{B},B=\bar{A}$
**2.運算律**
(1) 交換律：$A\bigcup B=B\bigcup A,A\bigcap B=B\bigcap A$
(2) 結合律：$(A\bigcup B)\bigcup C=A\bigcup (B\bigcup C)$
(3) 分配律：$(A\bigcap B)\bigcap C=A\bigcap (B\bigcap C)$
**3.德$\centerdot $摩根律**

$\overline{A\bigcup B}=\bar{A}\bigcap \bar{B}$                 $\overline{A\bigcap B}=\bar{A}\bigcup \bar{B}$
**4.完全事件組** 

${{A}_{1}}{{A}_{2}}\cdots {{A}_{n}}$兩兩互斥，且和事件為必然事件，即${{A}_{i}}\bigcap {{A}_{j}}=\varnothing, i\ne j ,\underset{i=1}{\overset{n}{\mathop \bigcup }}\,=\Omega $

**5.機率的基本公式**
(1)條件機率:
 $P(B|A)=\frac{P(AB)}{P(A)}$,表示$A$發生的條件下，$B$發生的機率。
(2)全機率公式：
$P(A)=\sum\limits_{i=1}^{n}{P(A|{{B}_{i}})P({{B}_{i}}),{{B}_{i}}{{B}_{j}}}=\varnothing ,i\ne j,\underset{i=1}{\overset{n}{\mathop{\bigcup }}}\,{{B}_{i}}=\Omega $
(3) Bayes公式：

$P({{B}_{j}}|A)=\frac{P(A|{{B}_{j}})P({{B}_{j}})}{\sum\limits_{i=1}^{n}{P(A|{{B}_{i}})P({{B}_{i}})}},j=1,2,\cdots ,n$
註：上述公式中事件${{B}_{i}}$的個數可為可列個。
(4)乘法公式：
$P({{A}_{1}}{{A}_{2}})=P({{A}_{1}})P({{A}_{2}}|{{A}_{1}})=P({{A}_{2}})P({{A}_{1}}|{{A}_{2}})$
$P({{A}_{1}}{{A}_{2}}\cdots {{A}_{n}})=P({{A}_{1}})P({{A}_{2}}|{{A}_{1}})P({{A}_{3}}|{{A}_{1}}{{A}_{2}})\cdots P({{A}_{n}}|{{A}_{1}}{{A}_{2}}\cdots {{A}_{n-1}})$

**6.事件的獨立性**
(1)$A$與$B$相互獨立$\Leftrightarrow P(AB)=P(A)P(B)$
(2)$A$，$B$，$C$兩兩獨立
$\Leftrightarrow P(AB)=P(A)P(B)$;$P(BC)=P(B)P(C)$ ;$P(AC)=P(A)P(C)$;
(3)$A$，$B$，$C$相互獨立
$\Leftrightarrow P(AB)=P(A)P(B)$;     $P(BC)=P(B)P(C)$ ;
$P(AC)=P(A)P(C)$  ;   $P(ABC)=P(A)P(B)P(C)$

**7.獨立重複試驗** 

將某試驗獨立重複$n$次，若每次實驗中事件A發生的機率為$p$，則$n$次試驗中$A$發生$k$次的機率為：
$P(X=k)=C_{n}^{k}{{p}^{k}}{{(1-p)}^{n-k}}$
**8.重要公式與結論**
$(1)P(\bar{A})=1-P(A)$
$(2)P(A\bigcup B)=P(A)+P(B)-P(AB)$
   $P(A\bigcup B\bigcup C)=P(A)+P(B)+P(C)-P(AB)-P(BC)-P(AC)+P(ABC)$
$(3)P(A-B)=P(A)-P(AB)$
$(4)P(A\bar{B})=P(A)-P(AB),P(A)=P(AB)+P(A\bar{B}),$
 $P(A\bigcup B)=P(A)+P(\bar{A}B)=P(AB)+P(A\bar{B})+P(\bar{A}B)$
(5)條件機率$P(\centerdot |B)$滿足機率的所有性質，
例如：. $P({{\bar{A}}_{1}}|B)=1-P({{A}_{1}}|B)$
$P({{A}_{1}}\bigcup {{A}_{2}}|B)=P({{A}_{1}}|B)+P({{A}_{2}}|B)-P({{A}_{1}}{{A}_{2}}|B)$
$P({{A}_{1}}{{A}_{2}}|B)=P({{A}_{1}}|B)P({{A}_{2}}|{{A}_{1}}B)$
(6)若${{A}_{1}},{{A}_{2}},\cdots ,{{A}_{n}}$相互獨立，則$P(\bigcap\limits_{i=1}^{n}{{{A}_{i}}})=\prod\limits_{i=1}^{n}{P({{A}_{i}})},$
 $P(\bigcup\limits_{i=1}^{n}{{{A}_{i}}})=\prod\limits_{i=1}^{n}{(1-P({{A}_{i}}))}$
(7)互斥、互逆與獨立性之間的關係：
$A$與$B$互逆$\Rightarrow$ $A$與$B$互斥，但反之不成立，$A$與$B$互斥（或互逆）且均非零機率事件$\Rightarrow $$A$與$B$不獨立.
(8)若${{A}_{1}},{{A}_{2}},\cdots ,{{A}_{m}},{{B}_{1}},{{B}_{2}},\cdots ,{{B}_{n}}$相互獨立，則$f({{A}_{1}},{{A}_{2}},\cdots ,{{A}_{m}})$與$g({{B}_{1}},{{B}_{2}},\cdots ,{{B}_{n}})$也相互獨立，其中$f(\centerdot ),g(\centerdot )$分別表示對相應事件做任意事件運算後所得的事件，另外，機率為1（或0）的事件與任何事件相互獨立.



#### 隨機變數及其機率分布

**1.隨機變數及機率分布**

取值帶有隨機性的變數，嚴格地說是定義在樣本空間上，取值於實數的函數稱為隨機變數，機率分布通常指分布函數或分布律

**2.分布函數的概念與性質**

定義： $F(x) = P(X \leq x), - \infty < x < + \infty$

性質：(1)$0 \leq F(x) \leq 1$ 

(2) $F(x)$單調不減

(3) 右連續$F(x + 0) = F(x)$ 

(4) $F( - \infty) = 0,F( + \infty) = 1$

**3.離散型隨機變數的機率分布**

$P(X = x_{i}) = p_{i},i = 1,2,\cdots,n,\cdots\quad\quad p_{i} \geq 0,\sum_{i =1}^{\infty}p_{i} = 1$

**4.連續型隨機變數的機率密度**

機率密度$f(x)$;非負可積，且:

(1)$f(x) \geq 0,$ 

(2)$\int_{- \infty}^{+\infty}{f(x){dx} = 1}$ 

(3)$x$為$f(x)$的連續點，則:

$f(x) = F'(x)$分布函數$F(x) = \int_{- \infty}^{x}{f(t){dt}}$

**5.常見分布**

(1) 0-1分布:$P(X = k) = p^{k}{(1 - p)}^{1 - k},k = 0,1$

(2) 二項分布:$B(n,p)$： $P(X = k) = C_{n}^{k}p^{k}{(1 - p)}^{n - k},k =0,1,\cdots,n$

(3) **Poisson**分布:$p(\lambda)$： $P(X = k) = \frac{\lambda^{k}}{k!}e^{-\lambda},\lambda > 0,k = 0,1,2\cdots$

(4) 均勻分布$U(a,b)$：$f(x) = \{ \begin{matrix}  & \frac{1}{b - a},a < x< b \\  & 0, \\ \end{matrix} $

(5) 正態分布:$N(\mu,\sigma^{2}):$ $\varphi(x) =\frac{1}{\sqrt{2\pi}\sigma}e^{- \frac{{(x - \mu)}^{2}}{2\sigma^{2}}},\sigma > 0,\infty < x < + \infty$

(6)指數分布:$E(\lambda):f(x) =\{ \begin{matrix}  & \lambda e^{-{λx}},x > 0,\lambda > 0 \\  & 0, \\ \end{matrix} $

(7)幾何分布:$G(p):P(X = k) = {(1 - p)}^{k - 1}p,0 < p < 1,k = 1,2,\cdots.$

(8)超幾何分布: $H(N,M,n):P(X = k) = \frac{C_{M}^{k}C_{N - M}^{n -k}}{C_{N}^{n}},k =0,1,\cdots,min(n,M)$

**6.隨機變數函數的機率分布**

(1)離散型：$P(X = x_{1}) = p_{i},Y = g(X)$

則: $P(Y = y_{j}) = \sum_{g(x_{i}) = y_{i}}^{}{P(X = x_{i})}$

(2)連續型：$X\tilde{\ }f_{X}(x),Y = g(x)$

則:$F_{y}(y) = P(Y \leq y) = P(g(X) \leq y) = \int_{g(x) \leq y}^{}{f_{x}(x)dx}$， $f_{Y}(y) = F'_{Y}(y)$

**7.重要公式與結論**

(1) $X\sim N(0,1) \Rightarrow \varphi(0) = \frac{1}{\sqrt{2\pi}},\Phi(0) =\frac{1}{2},$ $\Phi( - a) = P(X \leq - a) = 1 - \Phi(a)$

(2) $X\sim N\left( \mu,\sigma^{2} \right) \Rightarrow \frac{X -\mu}{\sigma}\sim N\left( 0,1 \right),P(X \leq a) = \Phi(\frac{a -\mu}{\sigma})$

(3) $X\sim E(\lambda) \Rightarrow P(X > s + t|X > s) = P(X > t)$

(4) $X\sim G(p) \Rightarrow P(X = m + k|X > m) = P(X = k)$

(5) 離散型隨機變數的分布函數為階梯間斷函數；連續型隨機變數的分布函數為連續函數，但不一定為處處可導函數。

(6) 存在既非離散也非連續型隨機變數。

#### 多維隨機變數及其分布

**1.二維隨機變數及其聯合分布**

由兩個隨機變數構成的隨機向量$(X,Y)$， 聯合分布為$F(x,y) = P(X \leq x,Y \leq y)$

**2.二維離散型隨機變數的分布**

(1) 聯合機率分布律 $P\{ X = x_{i},Y = y_{j}\} = p_{{ij}};i,j =1,2,\cdots$

(2) 邊緣分布律 $p_{i \cdot} = \sum_{j = 1}^{\infty}p_{{ij}},i =1,2,\cdots$ $p_{\cdot j} = \sum_{i}^{\infty}p_{{ij}},j = 1,2,\cdots$

(3) 條件分布律 $P\{ X = x_{i}|Y = y_{j}\} = \frac{p_{{ij}}}{p_{\cdot j}}$
$P\{ Y = y_{j}|X = x_{i}\} = \frac{p_{{ij}}}{p_{i \cdot}}$

**3. 二維連續性隨機變數的密度**

(1) 聯合機率密度$f(x,y):$

1) $f(x,y) \geq 0$ 

2) $\int_{- \infty}^{+ \infty}{\int_{- \infty}^{+ \infty}{f(x,y)dxdy}} = 1$

(2) 分布函數：$F(x,y) = \int_{- \infty}^{x}{\int_{- \infty}^{y}{f(u,v)dudv}}$

(3) 邊緣機率密度： $f_{X}\left( x \right) = \int_{- \infty}^{+ \infty}{f\left( x,y \right){dy}}$ $f_{Y}(y) = \int_{- \infty}^{+ \infty}{f(x,y)dx}$

(4) 條件機率密度：$f_{X|Y}\left( x \middle| y \right) = \frac{f\left( x,y \right)}{f_{Y}\left( y \right)}$ $f_{Y|X}(y|x) = \frac{f(x,y)}{f_{X}(x)}$

**4.常見二維隨機變數的聯合分布**

(1) 二維均勻分布：$(x,y) \sim U(D)$ ,$f(x,y) = \begin{cases} \frac{1}{S(D)},(x,y) \in D \\   0,其他  \end{cases}$

(2) 二維正態分布：$(X,Y)\sim N(\mu_{1},\mu_{2},\sigma_{1}^{2},\sigma_{2}^{2},\rho)$,$(X,Y)\sim N(\mu_{1},\mu_{2},\sigma_{1}^{2},\sigma_{2}^{2},\rho)$

$f(x,y) = \frac{1}{2\pi\sigma_{1}\sigma_{2}\sqrt{1 - \rho^{2}}}.\exp\left\{ \frac{- 1}{2(1 - \rho^{2})}\lbrack\frac{{(x - \mu_{1})}^{2}}{\sigma_{1}^{2}} - 2\rho\frac{(x - \mu_{1})(y - \mu_{2})}{\sigma_{1}\sigma_{2}} + \frac{{(y - \mu_{2})}^{2}}{\sigma_{2}^{2}}\rbrack \right\}$

**5.隨機變數的獨立性和相關性**

$X$和$Y$的相互獨立:$\Leftrightarrow F\left( x,y \right) = F_{X}\left( x \right)F_{Y}\left( y \right)$:

$\Leftrightarrow p_{{ij}} = p_{i \cdot} \cdot p_{\cdot j}$（離散型）
$\Leftrightarrow f\left( x,y \right) = f_{X}\left( x \right)f_{Y}\left( y \right)$（連續型）

$X$和$Y$的相關性：

相關係數$\rho_{{XY}} = 0$時，稱$X$和$Y$不相關，
否則稱$X$和$Y$相關

**6.兩個隨機變數簡單函數的機率分布**

離散型： $P\left( X = x_{i},Y = y_{i} \right) = p_{{ij}},Z = g\left( X,Y \right)$ 則：

$P(Z = z_{k}) = P\left\{ g\left( X,Y \right) = z_{k} \right\} = \sum_{g\left( x_{i},y_{i} \right) = z_{k}}^{}{P\left( X = x_{i},Y = y_{j} \right)}$

連續型： $\left( X,Y \right) \sim f\left( x,y \right),Z = g\left( X,Y \right)$
則：

$F_{z}\left( z \right) = P\left\{ g\left( X,Y \right) \leq z \right\} = \iint_{g(x,y) \leq z}^{}{f(x,y)dxdy}$，$f_{z}(z) = F'_{z}(z)$

**7.重要公式與結論**

(1) 邊緣密度公式： $f_{X}(x) = \int_{- \infty}^{+ \infty}{f(x,y)dy,}$
$f_{Y}(y) = \int_{- \infty}^{+ \infty}{f(x,y)dx}$

(2) $P\left\{ \left( X,Y \right) \in D \right\} = \iint_{D}^{}{f\left( x,y \right){dxdy}}$

(3) 若$(X,Y)$服從二維正態分布$N(\mu_{1},\mu_{2},\sigma_{1}^{2},\sigma_{2}^{2},\rho)$
則有：

1) $X\sim N\left( \mu_{1},\sigma_{1}^{2} \right),Y\sim N(\mu_{2},\sigma_{2}^{2}).$

2) $X$與$Y$相互獨立$\Leftrightarrow \rho = 0$，即$X$與$Y$不相關。

3) $C_{1}X + C_{2}Y\sim N(C_{1}\mu_{1} + C_{2}\mu_{2},C_{1}^{2}\sigma_{1}^{2} + C_{2}^{2}\sigma_{2}^{2} + 2C_{1}C_{2}\sigma_{1}\sigma_{2}\rho)$

4) ${\ X}$關於$Y=y$的條件分布為： $N(\mu_{1} + \rho\frac{\sigma_{1}}{\sigma_{2}}(y - \mu_{2}),\sigma_{1}^{2}(1 - \rho^{2}))$

5) $Y$關於$X = x$的條件分布為： $N(\mu_{2} + \rho\frac{\sigma_{2}}{\sigma_{1}}(x - \mu_{1}),\sigma_{2}^{2}(1 - \rho^{2}))$

(4) 若$X$與$Y$獨立，且分別服從$N(\mu_{1},\sigma_{1}^{2}),N(\mu_{1},\sigma_{2}^{2}),$
則：$\left( X,Y \right)\sim N(\mu_{1},\mu_{2},\sigma_{1}^{2},\sigma_{2}^{2},0),$

$C_{1}X + C_{2}Y\tilde{\ }N(C_{1}\mu_{1} + C_{2}\mu_{2},C_{1}^{2}\sigma_{1}^{2} C_{2}^{2}\sigma_{2}^{2}).$

(5) 若$X$與$Y$相互獨立，$f\left( x \right)$和$g\left( x \right)$為連續函數， 則$f\left( X \right)$和$g(Y)$也相互獨立。

#### 隨機變數的數字特徵

**1.數學期望**

離散型：$P\left\{ X = x_{i} \right\} = p_{i},E(X) = \sum_{i}^{}{x_{i}p_{i}}$；

連續型： $X\sim f(x),E(X) = \int_{- \infty}^{+ \infty}{xf(x)dx}$

性質：

(1) $E(C) = C,E\lbrack E(X)\rbrack = E(X)$

(2) $E(C_{1}X + C_{2}Y) = C_{1}E(X) + C_{2}E(Y)$

(3) 若$X$和$Y$獨立，則$E(XY) = E(X)E(Y)$ 

(4)$\left\lbrack E(XY) \right\rbrack^{2} \leq E(X^{2})E(Y^{2})$

**2.方差**：$D(X) = E\left\lbrack X - E(X) \right\rbrack^{2} = E(X^{2}) - \left\lbrack E(X) \right\rbrack^{2}$

**3.標準差**：$\sqrt{D(X)}$，

**4.離散型：**$D(X) = \sum_{i}^{}{\left\lbrack x_{i} - E(X) \right\rbrack^{2}p_{i}}$

**5.連續型：**$D(X) = {\int_{- \infty}^{+ \infty}\left\lbrack x - E(X) \right\rbrack}^{2}f(x)dx$

性質：

(1)$\ D(C) = 0,D\lbrack E(X)\rbrack = 0,D\lbrack D(X)\rbrack = 0$

(2) $X$與$Y$相互獨立，則$D(X \pm Y) = D(X) + D(Y)$

(3)$\ D\left( C_{1}X + C_{2} \right) = C_{1}^{2}D\left( X \right)$

(4) 一般有 $D(X \pm Y) = D(X) + D(Y) \pm 2Cov(X,Y) = D(X) + D(Y) \pm 2\rho\sqrt{D(X)}\sqrt{D(Y)}$

(5)$\ D\left( X \right) < E\left( X - C \right)^{2},C \neq E\left( X \right)$

(6)$\ D(X) = 0 \Leftrightarrow P\left\{ X = C \right\} = 1$

**6.隨機變數函數的數學期望**

(1) 對於函數$Y = g(x)$

$X$為離散型：$P\{ X = x_{i}\} = p_{i},E(Y) = \sum_{i}^{}{g(x_{i})p_{i}}$；

$X$為連續型：$X\sim f(x),E(Y) = \int_{- \infty}^{+ \infty}{g(x)f(x)dx}$

(2) $Z = g(X,Y)$;$\left( X,Y \right)\sim P\{ X = x_{i},Y = y_{j}\} = p_{{ij}}$; $E(Z) = \sum_{i}^{}{\sum_{j}^{}{g(x_{i},y_{j})p_{{ij}}}}$ $\left( X,Y \right)\sim f(x,y)$;$E(Z) = \int_{- \infty}^{+ \infty}{\int_{- \infty}^{+ \infty}{g(x,y)f(x,y)dxdy}}$

**7.協方差** 

$Cov(X,Y) = E\left\lbrack (X - E(X)(Y - E(Y)) \right\rbrack$

**8.相關係數**

 $\rho_{{XY}} = \frac{Cov(X,Y)}{\sqrt{D(X)}\sqrt{D(Y)}}$,$k$階原點矩 $E(X^{k})$;
$k$階中心矩 $E\left\{ {\lbrack X - E(X)\rbrack}^{k} \right\}$

性質：

(1)$\ Cov(X,Y) = Cov(Y,X)$

(2)$\ Cov(aX,bY) = abCov(Y,X)$

(3)$\ Cov(X_{1} + X_{2},Y) = Cov(X_{1},Y) + Cov(X_{2},Y)$

(4)$\ \left| \rho\left( X,Y \right) \right| \leq 1$

(5) $\ \rho\left( X,Y \right) = 1 \Leftrightarrow P\left( Y = aX + b \right) = 1$ ，其中$a > 0$

$\rho\left( X,Y \right) = - 1 \Leftrightarrow P\left( Y = aX + b \right) = 1$
，其中$a < 0$

**9.重要公式與結論**

(1)$\ D(X) = E(X^{2}) - E^{2}(X)$

(2)$\ Cov(X,Y) = E(XY) - E(X)E(Y)$

(3) $\left| \rho\left( X,Y \right) \right| \leq 1,$且 $\rho\left( X,Y \right) = 1 \Leftrightarrow P\left( Y = aX + b \right) = 1$，其中$a > 0$

$\rho\left( X,Y \right) = - 1 \Leftrightarrow P\left( Y = aX + b \right) = 1$，其中$a < 0$

(4) 下面5個條件互為充要條件：

$\rho(X,Y) = 0$ $\Leftrightarrow Cov(X,Y) = 0$ $\Leftrightarrow E(X,Y) = E(X)E(Y)$ $\Leftrightarrow D(X + Y) = D(X) + D(Y)$ $\Leftrightarrow  D(X - Y) = D(X) + D(Y)$

註：$X$與$Y$獨立為上述5個條件中任何一個成立的充分條件，但非必要條件。

#### 數理統計的基本概念

**1.基本概念**

總體：研究對象的全體，它是一個隨機變數，用$X$表示。

個體：組成總體的每個基本元素。

簡單隨機樣本：來自總體$X$的$n$個相互獨立且與總體同分布的隨機變數$X_{1},X_{2}\cdots,X_{n}$，稱為容量為$n$的簡單隨機樣本，簡稱樣本。

統計量：設$X_{1},X_{2}\cdots,X_{n},$是來自總體$X$的一個樣本，$g(X_{1},X_{2}\cdots,X_{n})$）是樣本的連續函數，且$g()$中不含任何未知參數，則稱$g(X_{1},X_{2}\cdots,X_{n})$為統計量。

樣本均值：$\overline{X} = \frac{1}{n}\sum_{i = 1}^{n}X_{i}$

樣本方差：$S^{2} = \frac{1}{n - 1}\sum_{i = 1}^{n}{(X_{i} - \overline{X})}^{2}$

樣本矩：樣本$k$階原點矩：$A_{k} = \frac{1}{n}\sum_{i = 1}^{n}X_{i}^{k},k = 1,2,\cdots$

樣本$k$階中心矩：$B_{k} = \frac{1}{n}\sum_{i = 1}^{n}{(X_{i} - \overline{X})}^{k},k = 1,2,\cdots$

**2.分布**

$\chi^{2}$分布：$\chi^{2} = X_{1}^{2} + X_{2}^{2} + \cdots + X_{n}^{2}\sim\chi^{2}(n)$，其中$X_{1},X_{2}\cdots,X_{n},$相互獨立，且同服從$N(0,1)$

$t$分布：$T = \frac{X}{\sqrt{Y/n}}\sim t(n)$ ，其中$X\sim N\left( 0,1 \right),Y\sim\chi^{2}(n),$且$X$，$Y$ 相互獨立。

$F$分布：$F = \frac{X/n_{1}}{Y/n_{2}}\sim F(n_{1},n_{2})$，其中$X\sim\chi^{2}\left( n_{1} \right),Y\sim\chi^{2}(n_{2}),$且$X$，$Y$相互獨立。

分位數：若$P(X \leq x_{\alpha}) = \alpha,$則稱$x_{\alpha}$為$X$的$\alpha$分位數

**3.正態總體的常用樣本分布**

(1) 設$X_{1},X_{2}\cdots,X_{n}$為來自正態總體$N(\mu,\sigma^{2})$的樣本，

$\overline{X} = \frac{1}{n}\sum_{i = 1}^{n}X_{i},S^{2} = \frac{1}{n - 1}\sum_{i = 1}^{n}{{(X_{i} - \overline{X})}^{2},}$則：

1) $\overline{X}\sim N\left( \mu,\frac{\sigma^{2}}{n} \right){\ \ }$或者$\frac{\overline{X} - \mu}{\frac{\sigma}{\sqrt{n}}}\sim N(0,1)$

2) $\frac{(n - 1)S^{2}}{\sigma^{2}} = \frac{1}{\sigma^{2}}\sum_{i = 1}^{n}{{(X_{i} - \overline{X})}^{2}\sim\chi^{2}(n - 1)}$

3) $\frac{1}{\sigma^{2}}\sum_{i = 1}^{n}{{(X_{i} - \mu)}^{2}\sim\chi^{2}(n)}$

4)${\ \ }\frac{\overline{X} - \mu}{S/\sqrt{n}}\sim t(n - 1)$

**4.重要公式與結論**

(1) 對於$\chi^{2}\sim\chi^{2}(n)$，有$E(\chi^{2}(n)) = n,D(\chi^{2}(n)) = 2n;$

(2) 對於$T\sim t(n)$，有$E(T) = 0,D(T) = \frac{n}{n - 2}(n > 2)$；

(3) 對於$F\tilde{\ }F(m,n)$，有 $\frac{1}{F}\sim F(n,m),F_{a/2}(m,n) = \frac{1}{F_{1 - a/2}(n,m)};$

(4) 對於任意總體$X$，有 $E(\overline{X}) = E(X),E(S^{2}) = D(X),D(\overline{X}) = \frac{D(X)}{n}$

