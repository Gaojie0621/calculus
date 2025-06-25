---

---

## 1. Trigonometry
![[trigonometry_angle_figure1.png]]

### 1.1  Angles

$$
\theta = \frac{a}{r}
$$
$$
a = \theta{r}
$$

### 1.2 The Trigonometric functions
$$
\sin \theta = \frac{y}{r}, \quad
\csc \theta = \frac{r}{y}, \quad
$$
$$
\cos \theta = \frac{x}{r}, \quad
\sec \theta = \frac{r}{x}, \quad
$$
$$
\tan \theta = \frac{y}{x}, \quad
\cot \theta = \frac{x}{y}
$$
### 1.3 Trigonometric identities
$$
\begin{array}{|c|c|}
\hline
\textbf{Function} & \textbf{Identity} \\
\hline
\csc \theta & \displaystyle \frac{1}{\sin \theta} \\
\sec \theta & \displaystyle \frac{1}{\cos \theta} \\
\cot \theta & \displaystyle \frac{1}{\tan \theta} \\
\tan \theta & \displaystyle \frac{\sin \theta}{\cos \theta} \\
\cot \theta & \displaystyle \frac{\cos \theta}{\sin \theta} \\
\hline
\end{array}
$$

$$
\begin{array}{|c|c|}
\hline
\textbf{Identity} & \textbf{Equation} \\
\hline
\text{Pythagorean Identity 1} & \sin^2 \theta + \cos^2 \theta = 1 \\
\text{Pythagorean Identity 2} & \tan^2 \theta + 1 = \sec^2 \theta \\
\text{Pythagorean Identity 3} & 1 + \cot^2 \theta = \csc^2 \theta \\
\hline
\end{array}
$$
 - **Sum and Difference Formulas**

$$
\begin{aligned}
\sin(x + y) &= \sin x \cos y + \cos x \sin y \\
\sin(x - y) &= \sin x \cos y - \cos x \sin y \\
\cos(x + y) &= \cos x \cos y - \sin x \sin y \\
\cos(x - y) &= \cos x \cos y + \sin x \sin y \\
\tan(x + y) &= \frac{\tan x + \tan y}{1 - \tan x \tan y} \\
\tan(x - y) &= \frac{\tan x - \tan y}{1 + \tan x \tan y}
\end{aligned}
$$
 - **Double-Angle Identities**


$$
\begin{aligned}
\sin(2\theta) &= 2\sin\theta\cos\theta \\
\cos(2\theta) &= \cos^2\theta - \sin^2\theta \\
              &= 2\cos^2\theta - 1 \\
              &= 1 - 2\sin^2\theta \\
\tan(2\theta) &= \frac{2\tan\theta}{1 - \tan^2\theta}
\end{aligned}
$$



 - **Half-Angle Identities**

$$
\begin{aligned}
\sin\left(\frac{\theta}{2}\right) &= \pm \sqrt{\frac{1 - \cos\theta}{2}} \\
\cos\left(\frac{\theta}{2}\right) &= \pm \sqrt{\frac{1 + \cos\theta}{2}} \\
\tan\left(\frac{\theta}{2}\right) &= \pm \sqrt{\frac{1 - \cos\theta}{1 + \cos\theta}} \\
                                  &= \frac{\sin\theta}{1 + \cos\theta} \\
                                  &= \frac{1 - \cos\theta}{\sin\theta}
\end{aligned}
$$

 -  **product formulas**
 $$
\begin{aligned}
\sin x \sin y &= \frac{1}{2}[\cos(x - y) - \cos(x + y)] \\
\cos x \cos y &= \frac{1}{2}[\cos(x - y) + \cos(x + y)] \\
\sin x \cos y &= \frac{1}{2}[\sin(x + y) + \sin(x - y)] \\
\cos x \sin y &= \frac{1}{2}[\sin(x + y) - \sin(x - y)]
\end{aligned}
$$

$$
\begin{aligned}
\sin x + \sin y &= 2 \sin\left(\frac{x + y}{2}\right) \cos\left(\frac{x - y}{2}\right) \\
\sin x - \sin y &= 2 \cos\left(\frac{x + y}{2}\right) \sin\left(\frac{x - y}{2}\right) \\
\cos x + \cos y &= 2 \cos\left(\frac{x + y}{2}\right) \cos\left(\frac{x - y}{2}\right) \\
\cos x - \cos y &= -2 \sin\left(\frac{x + y}{2}\right) \sin\left(\frac{x - y}{2}\right)
\end{aligned}
$$
*Hint:
$$
\sin x = \sin\left(\frac{x+y}{2} + \frac{x-y}{2}\right), \quad
\sin y = \sin\left(\frac{x+y}{2} - \frac{x-y}{2}\right)
$$

![[trigonometry_graph_2.png]]

---
## 2. Sigma Notations

### Theorem: Properties of Summation

**Let $c$ be a constant. Then:**


$$
\sum_{i = m}^{n} c a_i = c \sum_{i = m}^{n} a_i
$$

$$
\sum_{i = m}^{n} (a_i + b_i) = \sum_{i = m}^{n} a_i + \sum_{i = m}^{n} b_i
$$

$$
\sum_{i = m}^{n} (a_i - b_i) = \sum_{i = m}^{n} a_i - \sum_{i = m}^{n} b_i
$$
### Theorem: Common Summation Formulas
Let  $c$  be a constant and $n$  a positive integer. Then:
$$
1. \sum_{i=1}^{n} 1 = n
$$
$$
2. \sum_{i=1}^{n} c = nc
$$
$$
3. \sum_{i=1}^{n} i = \frac{n(n + 1)}{2}
$$
$$
4. \sum_{i=1}^{n} i^2 = \frac{n(n + 1)(2n + 1)}{6}
$$
$$
5. \sum_{i=1}^{n} i^3 = \left( \frac{n(n + 1)}{2} \right)^2
$$
#### *5. Proof by Mathematical Induction*

We want to prove: $\sum_{i=1}^{n} i^3 = \left( \frac{n(n + 1)}{2} \right)^2$

  **Step 1: Base Case** (n = 1)

Left-hand side (LHS):  $\sum_{i=1}^{1} i^3 = 1^3 = 1$

Right-hand side (RHS):  $\left( \frac{1(1 + 1)}{2} \right)^2 = \left( \frac{2}{2} \right)^2 = 1$

✅ LHS = RHS, so the base case holds.

 **Step 2: Inductive Hypothesis**

Assume that the formula holds for \( n = k \), i.e.,

$$
\sum_{i=1}^{k} i^3 = \left( \frac{k(k + 1)}{2} \right)^2
$$

We need to prove that it also holds for \( n = k + 1 \), i.e.,

$$
\sum_{i=1}^{k+1} i^3 = \left( \frac{(k+1)(k+2)}{2} \right)^2
$$

 **Step 3: Inductive Step**

Start with the left-hand side for $n = k + 1$ :  $\sum_{i=1}^{k+1} i^3 = \left( \sum_{i=1}^{k} i^3 \right) + (k+1)^3$

Use the inductive hypothesis:

$$
= \left( \frac{k(k + 1)}{2} \right)^2 + (k + 1)^3 

= (k + 1)^2 \left[ \left( \frac{k}{2} \right)^2 + (k + 1) \right]
$$

Simplify inside the brackets:

$$
= (k + 1)^2 \left[ \frac{k^2}{4} + (k + 1) \right]
= (k + 1)^2 \left[ \frac{k^2 + 4k + 4}{4} \right]
= (k + 1)^2 \cdot \frac{(k + 2)^2}{4}
$$

So we have:

$$
\sum_{i=1}^{k+1} i^3 = \left( \frac{(k + 1)(k + 2)}{2} \right)^2
$$

✅ This matches the desired formula for \( n = k + 1 \).

**By the principle of mathematical induction, the identity**

$$
\sum_{i=1}^{n} i^3 = \left( \frac{n(n + 1)}{2} \right)^2
$$

**holds for all positive integers $n$.**

---
## 3. Equations, Inequalities, and Polynomials

### 3.1 Key Topics  
##### 3.1.1  Polynomial Equations
   - **Forms**:  
     - Linear: $ax + b = 0$  
     - Quadratic: $ax^2 + bx + c = 0$  
     - Higher-degree: $ax^n + \cdots + k = 0$  
   - **Solving Methods**:  
     - Factoring (common factors, difference of squares, trinomial patterns)  
     - Quadratic Formula:  
       $$
       x = \frac{-b \pm \sqrt{b^2 - 4ac}}{2a}
       $$  
     - Completing the Square  
     - Polynomial Division (Long Division or Synthetic Division) 
     - Rational Root Theorem: test rational values $\pm \frac{p}{q}$  
     - Descartes’ Rule of Signs: estimate number of positive/negative real roots  
     - Graphical methods 

---
#### *Rational Root Theorem (Rational Zero Test)*

Let the polynomial be:  
$$
P(x) = a_nx^n + \cdots + a_1x + a_0
$$

> [!NOTE] **Theorem:**
> If a rational number $\frac{p}{q}$  (in lowest terms) is a root of the polynomial, then:
> 
> - $p$ must divide the **constant term** $a_0$  
> - $q$ must divide the **leading coefficient** $a_n$

**Steps to Use the Rational Root Theorem:**

1. **List all possible rational root candidates**:  
   $$
   \text{Candidates} = \pm \frac{\text{factors of } a_0}{\text{factors of } a_n}
   $$

2. **Test each candidate**

**Example:**

Let:  
$$
P(x) = 2x^3 - 3x^2 - 11x + 6
$$

- Constant term: $a_0 = 6$  → factors: $\pm1, \pm2, \pm3, \pm6$
- Leading coefficient: $a_n = 2$→ factors: $\pm1, \pm2$
- Possible rational roots:  
  $$
  \pm1, \pm2, \pm3, \pm6, \pm\frac{1}{2}, \pm\frac{3}{2}
  $$

**Test roots:**
Assume we find \( x = 2 \) is a root.  
Then use **polynomial division** to factor:  
$$
P(x) = (x - 2)(2x^2 + x - 3)
$$
---
#### *Descartes’ Rule of Signs — Explanation*
**Descartes’ Rule of Signs** is a method to estimate the number of **positive** and **negative** real roots of a polynomial equation by examining the signs of its coefficients.

Consider a polynomial:  
$$
P(x) = a_n x^n + a_{n-1} x^{n-1} + \cdots + a_1 x + a_0
$$

##### i. Positive Real Roots

1. Count the number of **sign changes** in the coefficients of  $P(x)$  
(A sign change occurs when consecutive coefficients have opposite signs, e.g., from + to − or − to +.)  

2. The number of **positive real roots** is **equal to the number of sign changes or less than that by an even number** (i.e., number of sign changes − 2k, where  $k \geq 0$).


##### ii. Negative Real Roots

1. Substitute   $\boxed{x \to -x}$   to get  $\boxed{P(-x)}$

2. Count the number of **sign changes** in the coefficients of  $P(-x)$

3. The number of **negative real roots** is equal to the number of sign changes in  $P(-x)$  
or less by an even number.

#### Example

Let:  
$$
P(x) = x^3 - 4x^2 + 5x - 2
$$

- Coefficients of  $P(x)$  are  $[+1, -4, +5, -2]$  
	- Number of sign changes: 3  
	- Possible positive roots: 3 or 1 (3 minus an even number)

Compute  
$$
P(-x) = -x^3 - 4x^2 - 5x - 2
$$

- Coefficients of  $P(-x)$  are  $[-1, -4, -5, -2]$  
	- Number of sign changes: 0  
	- Possible negative roots: 0

#### Summary

- Sign changes in  $P(x)$  give possible positive roots.  
- Sign changes in  $P(-x)$  give possible negative roots.  
- The actual number of roots is the count or less by an even number.

---

##### 3.1.2  Fundamental Theorem of Algebra
   - Every non-zero single-variable polynomial of degree $n$ has exactly $n$ complex roots (counting multiplicity).  
   - **Corollary**: A real polynomial can be factored into linear and/or irreducible quadratic factors over the reals.


##### 3.1.3 Inequalities 
   - **Linear/Quadratic Inequalities**:  
     - Solve like equations and test intervals (sign charts)  
     - Use parabola shape and x-intercepts to determine sign regions  
   - **Polynomial/Rational Inequalities**:  
     - Identify critical points (roots and undefined points)  
     - Use sign charts or test points to determine solution intervals  
     - Always consider open vs closed intervals based on inequality symbols  
     - Write solution sets in interval notation  

##### 3.1.4  Special Polynomial Types
   - **Even and Odd degree**: affects end behavior  
   - **Symmetric Polynomials**: e.g., palindromic or reciprocal polynomials  
   - **Monic Polynomials**: leading coefficient is 1  
   - **Factored Form**: Useful for analyzing roots and graphing  

---

### 3.2 Connections to Calculus  

- **Graphing**:  
  - Roots are x-intercepts  
  - Multiplicity affects whether graph crosses or touches x-axis  
  - End behavior determined by degree and leading coefficient  

- **Limits & Asymptotic Behavior**:  
  Let $P(x)$ and $Q(x)$ be polynomials. As $x \to \infty$:  
  - If $\\deg(P) < \\deg(Q)$: $\lim \frac{P(x)}{Q(x)} = 0$  
  - If $\\deg(P) = \\deg(Q)$: limit is the ratio of leading coefficients  
  - If $\\deg(P) > \\deg(Q)$: $\lim \frac{P(x)}{Q(x)} = \infty$ or DNE (slant asymptote may exist)

---

## 4. Graphs of Second-Degree Equations

### 4.1 circles

**Equation of a Circle** :
**$$(x - a)^2 + (y - b)^2 = r^2$$

```tikz
\begin{document}
  \begin{tikzpicture}[scale=1.0]
	% 坐标系
	\draw[->] (-3,0) -- (3,0) node[right] {$x$};
	\draw[->] (0,-3) -- (0,3) node[above] {$y$};
	
	% 圆（参数化样式）
	\draw[thick, blue] (1,1) circle (1.5cm) 
		node at (1,2.7) {$(x-1)^2 + (y-1)^2 = 2.25$};
	
	% 圆心标记
	\fill[red] (1,1) circle (2pt) node[below left] {$(1,1)$};
	\end{tikzpicture}
\end{document}
```


### 4.2 Parabolas

 -  $y = ax^2$
 

```tikz
\begin{document}
\begin{tikzpicture}[scale=1.0]
  % 坐标系（扩大y轴范围）
  \draw[->] (-3,0) -- (3,0) node[right] {$x$};
  \draw[->] (0,-5) -- (0,5) node[above] {$y$};
  
  % 四组抛物线（智能标签定位）
  \foreach \a/\color/\pos in {
    1.5/red/0.8,
    3.0/blue/0.6,
    -1.5/orange/-0.8,
    -3.0/purple/-0.6
  }{
    \draw[\color, thick, domain=-{sqrt(5/abs(\a))}:{sqrt(5/abs(\a))}] 
      plot (\x, \a*\x*\x);
    \node[\color, anchor=west] at (1.2, \a*1.44) {$y = \a x^2$};
  }

  % 顶点标记
  \foreach \a/\color in {1.5/red, 3.0/blue, -1.5/orange, -3.0/purple}
    \fill[\color] (0,0) circle (1.5pt);
\end{tikzpicture}
\end{document}
```

 
 - $x = ay^2$
```tikz
\begin{document}
\begin{tikzpicture}[scale=1.0]
  % 坐标系（扩大y轴范围）
  \draw[->] (-3,0) -- (3,0) node[right] {$x$};
  \draw[->] (0,-5) -- (0,5) node[above] {$y$};
  
  % 四组抛物线（智能标签定位）
  \foreach \a/\color/\pos in {
    1.5/red/0.8,
    3.0/blue/0.6,
    -1.5/orange/-0.8,
    -3.0/purple/-0.6
  }{
    \draw[\color, thick, domain=-{sqrt(5/abs(\a))}:{sqrt(5/abs(\a))}] 
      plot (\a*\x*\x, \x);
    \node[\color, anchor=west] at (\a*\pos*\pos, \pos) {$x = \a y^2$};
  }

  % 顶点标记
  \foreach \a/\color in {1.5/red, 3.0/blue, -1.5/orange, -3.0/purple}
    \fill[\color] (0,0) circle (1.5pt);
\end{tikzpicture}
\end{document}
```

**"The larger the value of _a_, the narrower the opening."**


### 4.3 Ellipses

 - **Horizontal major axis:**

$$
\frac{x^2}{a^2} + \frac{y^2}{b^2} = 1 \quad (a > b)
$$

```tikz
\begin{document}
\begin{tikzpicture}[scale=1.2]
\usetikzlibrary{decorations.pathreplacing}
  % 坐标系
  \draw[->] (-3,0) -- (3,0) node[right] {$x$};
  \draw[->] (0,-2) -- (0,2) node[above] {$y$};
  
  % 椭圆参数 (a > b)
  \def\a{2}    % 水平轴半径
  \def\b{1}    % 垂直轴半径
  \def\h{0}    % 中心x
  \def\k{0}    % 中心y

  % 绘制椭圆
  \draw[red, thick] (\h,\k) ellipse (\a cm and \b cm);
  
  % 标注主轴
  \draw[decorate, decoration={brace, amplitude=5pt, mirror}] (\h,\k) -- (\h+\a,\k) node[midway,below] {$a$};
  \draw[decorate, decoration={brace, amplitude=5pt}] (\h,\k) -- (\h,\k+\b) node[midway,left] {$b$};
  
  % 中心点
  \fill (\h,\k) circle (2pt) node[below left] {$(0,0)$};
  
  % 公式标注
  \node[anchor=north west] at (-2.8,1.8) {
    $\frac{x^2}{a^2} + \frac{y^2}{b^2} = 1$ \\
    $(a > b)$
  };
\end{tikzpicture}
\end{document}
```

```tikz

```
 - **Vertical major axis:**
$$ 
\frac{x^2}{b^2} + \frac{y^2}{a^2} = 1 \quad (a > b)
$$

```tikz
\begin{document}
\begin{tikzpicture}[scale=1.2]
  % 坐标系
  \draw[->] (-2,0) -- (2,0) node[right] {$x$};
  \draw[->] (0,-3) -- (0,3) node[above] {$y$};
  
  % 椭圆参数 (b > a)
  \def\a{0.8}  % 水平轴半径
  \def\b{2}    % 垂直轴半径
  \def\h{0}    % 中心x
  \def\k{0}    % 中心y

  % 绘制椭圆
  \draw[blue, thick] (\h,\k) ellipse (\a cm and \b cm);
  
  % 标注主轴
  \draw[dashed] (\h,\k) -- (\h+\a,\k) node[midway,below] {$a$};
  \draw[dashed] (\h,\k) -- (\h,\k+\b) node[midway,left] {$b$};
  
  % 公式标注
  \node[anchor=north west] at (-1.8,2.8) {
    $\frac{x^2}{a^2} + \frac{y^2}{b^2} = 1$ \\
    $ (b > a)$
  };
\end{tikzpicture}
\end{document}
```
 - **centered at (h, k):**    $\boxed{\frac{(x - h)^2}{a^2} + \frac{(y - k)^2}{b^2} = 1}$

```tikz
\begin{document}
\begin{tikzpicture}[scale=1.2]
  % 坐标系
  \draw[->] (-1,0) -- (5,0) node[right] {$x$};
  \draw[->] (0,-2) -- (0,4) node[above] {$y$};
  
  % 椭圆参数
  \def\a{1.5}  % 水平轴半径
  \def\b{1}    % 垂直轴半径
  \def\h{2}    % 中心x
  \def\k{1}    % 中心y

  % 绘制椭圆
  \draw[purple, thick] (\h,\k) ellipse (\a cm and \b cm);
  
  % 标注
  \draw[dashed, help lines] 
    (\h,\k) -- ++(\a,0) node[midway,above] {$a$}
    (\h,\k) -- ++(0,\b) node[midway,right] {$b$};
  
  % 中心点
  \fill (\h,\k) circle (2pt) node[below right] {$(h,k)$};
  
  % 公式标注
  \node[anchor=north west] at (3.5,3.5) {
    $\frac{(x-h)^2}{a^2} + \frac{(y-k)^2}{b^2} = 1$
  };
  
  % 辅助线
  \draw[gray, dotted] (\h,0) -- (\h,\k) node[midway,left] {$k$};
  \draw[gray, dotted] (0,\k) -- (\h,\k) node[midway,below] {$h$};
\end{tikzpicture}
\end{document}
```

---

## 5.  Elementary Functions

### 5.1 Core Function Types
#### 5.1.1 Exponential Functions
- **Definition**: $f(x) = a^x$ where $a > 0$ ($a \neq 1$)
- **Key Example**: $e^x$ (natural exponential)
- **Properties**:
  - Domain: $\mathbb{R}$
  - Range: $(0, +\infty)$
  - Always increasing if $a > 1$
  - Horizontal asymptote: $y = 0$

```tikz
\begin{document}
\begin{tikzpicture}[scale=1.5, >=stealth]
  % Axes
  \draw[->] (-3,0) -- (3,0) node[right] {$x$};
  \draw[->] (0,-0.5) -- (0,4) node[above] {$y$};
  
  % Grid (optional)
  \draw[gray!30, dashed] (-3,-0.5) grid (3,4);
  
  % Ticks
  \foreach \x in {-3,-2,-1,0,1,2,3}
    \draw (\x,0.1) -- (\x,-0.1) node[below] {\x};
  \foreach \y in {0,1,2,3,4}
    \draw (0.1,\y) -- (-0.1,\y) node[left] {\y};
  
  % Exponential functions
  \draw[blue, thick, domain=-3:1.5, smooth] plot (\x, {2^\x}) node[right] {$y = 2^x$}; % Growing exponential (a=2)
  \draw[red, thick, domain=-1.5:3, smooth] plot (\x, {0.5^\x}) node[right] {$y = 0.5^x$}; % Decaying exponential (a=0.5)
  
  % Highlight asymptote and intersection
  \draw[dashed] (-3,0) -- (3,0); % Asymptote at y=0
  \fill (0,1) circle (2pt) node[above left] {$(0,1)$}; % All exponentials pass through (0,1)
\end{tikzpicture}
\end{document}
```

#### *Natural Exponential Function*

##### Definition
The natural exponential function is defined as:
$$ y = e^x $$
where:
- $e \approx 2.71828$ (Euler's number)
- The function equals its own derivative: $\frac{dy}{dx} = e^x$
##### Key Properties
1. **Domain**: $(-\infty, \infty)$
2. **Range**: $(0, \infty)$
3. **y-intercept**: (0,1)
4. **Asymptote**: y=0 (horizontal)
5. **Always increasing**
6. **Concave up everywhere**
##### Special Property at (0,1)
The tangent line at x=0 has:
- Slope = $e^0 = 1$
- Equation: $y = x + 1$
##### Graph Visualization

```tikz
\begin{document}
\begin{tikzpicture}[scale=1.0]
  % Axes
  \draw[->] (-3,0) -- (3,0) node[right] {$x$};
  \draw[->] (0,-0.5) -- (0,5) node[above] {$y$};
  
  % Grid lines
  \foreach \x in {-2,-1,1,2} \draw[gray!20] (\x,-0.5) -- (\x,5);
  \foreach \y in {1,2,3,4} \draw[gray!20] (-3,\y) -- (3,\y);
  
  % Exponential curve (approximated)
  \draw[blue, thick, smooth] plot coordinates {
    (-2.5,0.08) (-2,0.13) (-1.5,0.22) (-1,0.37) 
    (-0.5,0.61) (0,1) (0.5,1.65) (1,2.72) 
    (1.5,4.48) 
  };
  \node[blue, right] at (1,3) {$y = e^x$};
  
  % Tangent line at (0,1): y = x + 1
  \draw[red, thick] (-2,-1) -- (2,3);
  \node[red, right] at (1,1.5) {Tangent: $y = x+1$};
  
  % Key point
  \fill (0,1) circle (2pt) node[below right] {$(0,1)$};
  
  % Asymptote
  \draw[orange, dashed] (-3,0) -- (3,0) node[right] {$y=0$};
\end{tikzpicture}
\end{document}
```

#### 5.1.2 Logarithmic Functions
- **Definition**: $f(x) = \log_a x$ (inverse of $a^x$)
- **Key Example**: $\ln x$ (natural log, base $e$)
- **Properties**:
  - Domain: $(0, +\infty)$
  - Range: $\mathbb{R}$
  - Vertical asymptote: $x = 0$
```tikz
\begin{document}
\begin{tikzpicture}[scale=1.2, >=stealth]
  % Axes
  \draw[->] (0,0) -- (5,0) node[right] {$x$};
  \draw[->] (0,-1) -- (0,2.5) node[above] {$y$};
  
  % Grid
  \draw[gray!30, dashed] (0,-1) grid (5,2.5);
  
  % Ticks
  \foreach \x in {0,1,2,3,4,5}
    \draw (\x,0.1) -- (\x,-0.1) node[below] {\x};
  \foreach \y in {-1,0,1,2}
    \draw (0.1,\y) -- (-0.1,\y) node[left] {\y};
  
  % Logarithmic functions
  \draw[blue, thick, domain=0.09:5, smooth] plot (\x, {ln(\x)/ln(2)});
  \node[blue, right] at (4, {ln(4)/ln(2)}) {$y = \log_2 x$};
  
  \draw[red, thick, domain=0.04:5, smooth] plot (\x, {ln(\x)/ln(3)});
  \node[red, right] at (4, {ln(4)/ln(3)}) {$y = \log_3 x$};
  
  \draw[green!70!black, thick, domain=0.02:5, smooth] plot (\x, {ln(\x)/ln(5)});
  \node[green!70!black, right] at (4, {ln(4)/ln(5)}) {$y = \log_5 x$};
  
  \draw[orange, thick, domain=0.02:5, smooth] plot (\x, {ln(\x)/ln(10)});
  \node[orange, right] at (4, {ln(4)/ln(10)}) {$y = \log_{10} x$};
  
  % Intersection point
  \fill (1,0) circle (2pt);
  \node[below right] at (1,0) {1};
\end{tikzpicture}
\end{document}
```


#### 5.1.3 Trigonometric Functions
- **Key Examples**:
  - $\sin x$: Periodic with period $2\pi$, range $[-1, 1]$
  - $\cos x$, $\tan x$ (similar analysis)
- **Properties**:
  - Amplitude (height): $|A|$ in $A\sin(Bx)$
  - Period: $\frac{2\pi}{|B|}$

#### 5.1.4 Power Functions
- **Definition**: $f(x) = x^n$ ($n \in \mathbb{R}$)
- **Examples**:
  - $x^2$: Parabola, domain $\mathbb{R}$, range $[0, +\infty)$
  - $\sqrt{x} = x^{1/2}$: Domain $[0, +\infty)$
 
 (i)  $a = n$, where $n$ is a positive integer:
 ![[elementary_functions_1.png]]
 (ii)  $a = \frac{1}{n}$, where $n$ is a positive integer:
 - The function $f(x) = x^{\frac{1}{n}} = \sqrt[n]{x}$ is a root function
![[elementary_functions_2.png]]
(iii) $a = -1$:
 - ***reciprocal function***: $f(x) = x^{-1} = \frac{1}{x}$

```tikz
\begin{document}
\begin{tikzpicture}[scale=1.0, >=stealth]
  % Axes
  \draw[->] (-3,0) -- (3,0) node[right] {$x$};
  \draw[->] (0,-3) -- (0,3) node[above] {$y$};
  
  % Grid (optional)
  \draw[gray!30, dashed] (-3,-3) grid (3,3);
  
  % Ticks
  \foreach \x in {-3,-2,-1,1,2,3}
    \draw (\x,0.1) -- (\x,-0.1) node[below] {$\x$};
  \foreach \y in {-3,-2,-1,1,2,3}
    \draw (0.1,\y) -- (-0.1,\y) node[left] {$\y$};
  
  % Reciprocal function (with asymptotes)
  \draw[blue, thick, domain=-3:-0.3, smooth] plot (\x, {1/\x}); % Left branch
  \draw[blue, thick, domain=0.3:3, smooth] plot (\x, {1/\x});  % Right branch
  \node[blue, right] at (1.5,0.7) {$y = \frac{1}{x}$};
  
  % Asymptotes
  \draw[dashed, red] (-3,0) -- (3,0) node[above left] {$y=0$}; % Horizontal
  \draw[dashed, red] (0,-3) -- (0,3) node[below right] {$x=0$}; % Vertical
\end{tikzpicture}
\end{document}
```


---

### 5.2 Function Transformations
For any function $y = f(x)$:
1. **Vertical Shift**: $y = f(x) + k$  
   - Up if $k > 0$, down if $k < 0$
```tikz
\begin{document}
\begin{tikzpicture}[scale=1.5, >=stealth]
  % Axes
  \draw[->] (-2.5,0) -- (2.5,0) node[right] {$x$};
  \draw[->] (0,-1.5) -- (0,4.5) node[above] {$y$};
  
  % Grid (optional)
  \draw[gray!30, dashed] (-2.5,-1.5) grid (2.5,4.5);
  
  % Ticks
  \foreach \x in {-2,-1,1,2}
    \draw (\x,0.1) -- (\x,-0.1) node[below] {$\x$};
  \foreach \y in {-1,0,1,2,3,4}
    \draw (0.1,\y) -- (-0.1,\y) node[left] {$\y$};
  
  % Original function: y = x^2 (black)
  \draw[black, thick, domain=-1.7:1.7, smooth] plot (\x, {\x*\x}) 
    node[right] {$y = x^2$};
  
  % Shifted functions
  \draw[blue, thick, domain=-1.7:1.7, smooth] plot (\x, {\x*\x + 2}) 
    node[right] {$y = x^2 + 2$}; % Shift up by 2
  \draw[red, thick, domain=-1.7:1.7, smooth] plot (\x, {\x*\x - 1}) 
    node[right] {$y = x^2 - 1$}; % Shift down by 1
  
  % Highlight shifts with arrows
  \draw[blue, ->, dashed] (1.2,1.44) -- (1.2,3.44) node[midway, right] {+2 units};
  \draw[red, ->, dashed] (-1.2,1.44) -- (-1.2,0.44) node[midway, left] {-1 unit};
\end{tikzpicture}
\end{document}
```
1. **Horizontal Shift**: $y = f(x - h)$  
   - Right if $h > 0$, left if $h < 0$
```tikz
\begin{document}
\begin{tikzpicture}[scale=1.5, >=stealth]
  % Axes
  \draw[->] (-2.5,0) -- (4.5,0) node[right] {$x$};
  \draw[->] (0,-0.5) -- (0,3) node[above] {$y$};
  
  % Grid
  \draw[gray!30, dashed] (-2.5,-0.5) grid (4.5,3);
  
  % Ticks
  \foreach \x in {-2,-1,0,1,2,3,4}
    \draw (\x,0.1) -- (\x,-0.1) node[below] {$\x$};
  \foreach \y in {0,1,2,3}
    \draw (0.1,\y) -- (-0.1,\y) node[left] {$\y$};
  
  % Original function
  \draw[black, thick, domain=0:4, samples=100] plot (\x, {sqrt(\x)});
  \node[black, right] at (4,2) {$y = \sqrt{x}$};
  
  % Shifted functions (corrected plotting method)
  \draw[blue, thick, domain=0:4, samples=100] plot ({\x+2}, {sqrt(\x)});
  \node[blue, right] at (4,1.5) {$y = \sqrt{x-2}$};
  
  \draw[red, thick, domain=0:4, samples=100] plot ({\x-1}, {sqrt(\x)});
  \node[red, right] at (3,2.5) {$y = \sqrt{x+1}$};
  
  % Shift arrows
  \draw[blue, ->, dashed] (1,1) -- (3,1) node[midway, above] {Right +2};
  \draw[red, ->, dashed] (1,1) -- (0,1) node[midway, above] {Left -1};
  
  % Origin
  \fill (0,0) circle (1pt) node[below left] {O};
\end{tikzpicture}
\end{document}
```

1. **Scaling**:
   - Vertical: $y = A f(x)$ (stretch if $|A| > 1$, shrink if $0 < |A| < 1$)
   - Horizontal: $y = f(Bx)$ (compressed if $|B| > 1$, stretched if $0 < |B| < 1$)
![[functions_3.png]]
1. **Reflection**:
   - $y = -f(x)$ (flip vertically)
   - $y = f(-x)$ (flip horizontally)

### 5.3 inverse functions and Logarithms
**Definition 1** 
A function f is called a ***one-to-one function*** if it never takes on
the same value twice; that is:
$$
f(x_{1}) \neq f(x_{2}) \quad whenever x_{1} \neq x_{2}
$$
***Horizontal Line Test***  A function is one-to-one if and only if no horizontal line
intersects its graph more than once.

```tikz
\begin{document}
\begin{tikzpicture}[scale=1.2]

% Failed horizontal line test example (not one-to-one)
\begin{scope}[shift={(0,0)}]
  % Axes
  \draw[->] (-2,0) -- (4,0) node[right] {$x$};
  \draw[->] (0,-1) -- (0,3) node[above] {$y$};
  
  % Function curve (parabola)
  \draw[blue, thick, domain=-1.5:3, smooth] plot (\x, {0.5*(\x-1)^2});
  \node[blue, right] at (3,2) {$y = f(x)$};
  
  % Horizontal line intersecting twice
  \draw[red, thick, dashed] (-1,1.25) -- (3,1.25) 
    node[midway, above] {Fails test};
  
  % Intersection points
  \filldraw (0.29,1.25) circle (1.5pt);
  \filldraw (1.71,1.25) circle (1.5pt);
  
  \node at (1,-1) {Not one-to-one (fails horizontal line test)};
\end{scope}

% Passed horizontal line test example (one-to-one)
\begin{scope}[shift={(7,0)}]
  % Axes
  \draw[->] (-2,0) -- (4,0) node[right] {$x$};
  \draw[->] (0,-1) -- (0,3) node[above] {$y$};
  
  % Function curve (exponential)
  \draw[blue, thick, domain=-1.5:1.5, smooth] plot (\x, {exp(\x)});
  \node[blue, right] at (1.5,4) {$y = g(x)$};
  
  % Horizontal line intersecting once
  \draw[green!70!black, thick, dashed] (-1,1.5) -- (3,1.5) 
    node[midway, above] {Passes test};
  
  % Single intersection point
  \filldraw (0.405,1.5) circle (1.5pt);
  
  \node at (1,-1) {One-to-one (passes test)};
\end{scope}

\end{tikzpicture}
\end{document}
```

**Definition 2** 
Let $f$ be a one-to-one function with domain $A$ and range $B$.  
Then its ***inverse function*** $f^{-1}$has domain $B$ and range $A$, and is defined by

$$
f^{-1}(y) = x \quad \text{if and only if} \quad f(x) = y
$$

for any $y \in B$.

**Definition 3**
- $f^{-1}(x) = y \iff f(y) = x$  

**Definition 4: cancellation equation**
- $f^{-1}(f(x)) = x$ for every $x \in A$  
- $f(f^{-1}(x)) = x$ for every $x \in B$

##### How to Find the Inverse Function of a One-to-One Function $f$

**Step 1**: Write the equation  
$$
y = f(x)
$$

**Step 2**: Solve this equation for $x$ in terms of $y$ (if possible): $\boxed{f(y) = x}$

**Step 3**: Interchange $x$ and $y$ to express $f^{-1}$ as a function of $x$:  
$$
y = f^{-1}(x)
$$
**Example**  
Find the inverse function of $f(x) = x^3 + 2$.

**Solution**  
According to the inverse function process:

1. Write  $y = x^3 + 2$

2. Solve for $x$ in terms of $y$ :   $x^3 = y - 2, \quad x = \sqrt[3]{y - 2}$

3. Interchange $x$ and $y$ :   $y = \sqrt[3]{x - 2}$

Therefore, the inverse function is:  
$$
f^{-1}(x) = \sqrt[3]{x - 2}
$$

#### Definition of Logarithm and its Inverse Relationship

- $\log_b x = y \iff b^y = x$  
- $\log_b(b^x) = x$ for every $x \in \mathbb{R}$  
- $b^{\log_b x} = x$ for every $x > 0$

#### Laws of Logarithms 
If $x$ and $y$ are **positive numbers**, and $r$ is any **real number**, then:

1. $\log_b(xy) = \log_b x + \log_b y$  
2. $\log_b\left(\dfrac{x}{y}\right) = \log_b x - \log_b y$  
3. $\log_b(x^r) = r \log_b x$

***Natural Logarithm and Its Inverse***

- $\log_e x = \ln x$  
- $\ln x = y \iff e^y = x$  
- $\ln(e^x) = x$ for every $x \in \mathbb{R}$  
- $e^{\ln x} = x$ for every $x > 0$  
- $\ln e = 1$

```tikz
\begin{document}
\begin{tikzpicture}[scale=1.0]

  % Axes
  \draw[->] (-3,0) -- (4,0) node[right] {$x$};
  \draw[->] (0,-3) -- (0,4) node[above] {$y$};
  \draw[dashed] (-3,-3) -- (4,4) node[right] {$y=x$};

  % Grid (light)
  \foreach \i in {-2,-1,1,2,3} {
    \draw[gray!20] (\i,-3) -- (\i,4);
    \draw[gray!20] (-3,\i) -- (4,\i);
  }

  % y = e^x (approximated points)
  \draw[blue, thick, smooth] plot coordinates {
    (-2.5,0.08) (-2,0.14) (-1.5,0.22) (-1,0.37) (-0.5,0.61)
    (0,1) (0.5,1.65) (1,2.72) (1.5,4.48)
  };
  \node[blue, right] at (1,3) {$y = e^x$};

  % y = ln(x) (approximated points)
  \draw[red, thick, smooth] plot coordinates {
    (0.05,-3) (0.1,-2.3) (0.22,-1.5) (0.37,-1) (0.61,-0.5)
    (1,0) (1.65,0.5) (2.72,1) (4.48,1.5)
  };
  \node[red, above] at (2.5,1) {$y = \ln x$};

  % Key points
  \fill (0,1) circle (2pt) node[left] {$(0,1)$};
  \fill (1,0) circle (2pt) node[below right] {$(1,0)$};
  \fill (1,2.72) circle (1.5pt);
  \fill (2.72,1) circle (1.5pt);

  % Reflection note
  \node[gray] at (2,-2) {Reflections across $y=x$};
\end{tikzpicture}
\end{document}
```

#### inverse Trigonometric functions
#### 1. $\arcsin x$

- **Definition**:  
    $y = \arcsin x \iff \sin y = x$
    
- **Domain**: $[-1, 1]$
    
- **Range**: $\left[ -\dfrac{\pi}{2}, \dfrac{\pi}{2} \right]$
#### 2. $\arccos x$

- **Definition**:  
    $y = \arccos x \iff \cos y = x$
    
- **Domain**: $[-1, 1]$
    
- **Range**: $[0, \pi]$
#### 3. $\arctan x$

- **Definition**:  
    $y = \arctan x \iff \tan y = x$
    
- **Domain**: $\mathbb{R}$
    
- **Range**: $\left( -\dfrac{\pi}{2}, \dfrac{\pi}{2} \right)$

```tikz
\begin{document}
\begin{tikzpicture}[scale=1.2]
  %%%%%%%%%%%%%%%%%%%%%% arcsin(x) %%%%%%%%%%%%%%%%%%%%%%
  \begin{scope}[xshift=0cm]
    % Axes
    \draw[->] (-1.5,0) -- (1.5,0) node[right] {$x$};
    \draw[->] (0,-1.7) -- (0,1.7) node[above] {$y$};
    \draw[dashed] (-1,-1.7) -- (-1,1.7);
    \draw[dashed] (1,-1.7) -- (1,1.7);
    
    % arcsin(x)
    \draw[blue, thick, smooth] plot coordinates {
      (-1,-1.57) (-0.8,-0.93) (-0.5,-0.52) (0,0) 
      (0.5,0.52) (0.8,0.93) (1,1.57)
    };
    
    % Labels
    \node[blue] at (0.6,1.2) {$\arcsin x$};
    \node at (1,-0.2) {$1$};
    \node at (-1,-0.2) {$-1$};
    \node at (0.2,1.57) {$\frac{\pi}{2}$};
    \node at (0.2,-1.57) {$-\frac{\pi}{2}$};
    \node at (0,-2.1) {(a) $y = \sin^{-1}x = \arcsin x$};
  \end{scope}

  %%%%%%%%%%%%%%%%%%%%%% arccos(x) %%%%%%%%%%%%%%%%%%%%%%
  \begin{scope}[xshift=4cm]
    % Axes
    \draw[->] (-1.5,0) -- (1.5,0) node[right] {$x$};
    \draw[->] (0,-0.5) -- (0,3.5) node[above] {$y$};
    \draw[dashed] (-1,-0.5) -- (-1,3.5);
    \draw[dashed] (1,-0.5) -- (1,3.5);
    
    % arccos(x)
    \draw[red, thick, smooth] plot coordinates {
      (-1,3.14) (-0.8,2.5) (-0.5,2.09) (0,1.57)
      (0.5,1.05) (0.8,0.64) (1,0)
    };
    
    % Labels
    \node[red] at (-0.6,2.8) {$\arccos x$};
    \node at (1,-0.2) {$1$};
    \node at (-1,-0.2) {$-1$};
    \node at (0.2,3.14) {$\pi$};
    \node at (0.2,1.57) {$\frac{\pi}{2}$};
    \node at (0,-0.8) {(b) $y = \cos^{-1}x =\arccos x$};
  \end{scope}

  %%%%%%%%%%%%%%%%%%%%%% arctan(x) %%%%%%%%%%%%%%%%%%%%%%
  \begin{scope}[xshift=9cm]
    % Axes
    \draw[->] (-2.5,0) -- (2.5,0) node[right] {$x$};
    \draw[->] (0,-1.7) -- (0,1.7) node[above] {$y$};
    
    % arctan(x)
    \draw[green!60!black, thick, smooth] plot coordinates {
      (-2.5,-1.19) (-2,-1.11) (-1,-0.79) (0,0)
      (1,0.79) (2,1.11) (2.5,1.19)
    };
    
    % Asymptotes
    \draw[dashed] (-2.5,1.57) -- (2.5,1.57);
    \draw[dashed] (-2.5,-1.57) -- (2.5,-1.57);
    
    % Labels
    \node[green!60!black] at (1.8,0.8) {$\arctan x$};
    \node at (0.2,1.57) {$\frac{\pi}{2}$};
    \node at (0.2,-1.57) {$-\frac{\pi}{2}$};
    \node at (0,-2.1) {(c) $y = \tan^{-1}x =\arctan x$};
  \end{scope}
\end{tikzpicture}
\end{document}
```


- **The inverse cosecant function:**
  $$
  y = \csc^{-1}(x) \quad (|x| > 1) \quad \Leftrightarrow \quad \csc(y) = x, \quad y \in \left[0, \frac{\pi}{2}\right) \cup \left(\frac{\pi}{2}, \pi\right]
  $$

- **The inverse secant function:**
  $$
  y = \sec^{-1}(x) \quad (|x| > 1) \quad \Leftrightarrow \quad \sec(y) = x, \quad y \in \left[0, \frac{\pi}{2}\right) \cup \left(\frac{\pi}{2}, \pi\right]
  $$

- **The inverse cotangent function:**
  $$
  y = \cot^{-1}(x) \quad (x \in \mathbb{R}) \quad \Leftrightarrow \quad \cot(y) = x, \quad y \in (0, \pi)
  $$
```tikz
\begin{document}
\begin{tikzpicture}[scale=0.85]
  %%%%%%%%%%%%%%%%%%%%%% arccsc(x) %%%%%%%%%%%%%%%%%%%%%%
  \begin{scope}[xshift=0cm]
    % Axes
    \draw[->] (-3.5,0) -- (3.5,0) node[right] {$x$};
    \draw[->] (0,-1.7) -- (0,1.7) node[above] {$y$};
    
    % arccsc(x) - blue
    \draw[blue, thick, smooth] plot coordinates {
      (-3.5,-0.29) (-2,-0.52) (-1,-1.57) (-0.5,-1.57)
      (0.5,1.57) (1,1.57) (2,0.52) (3.5,0.29)
    };
    
    % Discontinuity markers
    \draw[blue, fill=white] (-1,-1.57) circle (2pt);
    \draw[blue, fill=white] (1,1.57) circle (2pt);
    
    % Asymptotes and labels
    \draw[dashed] (-3.5,0) -- (3.5,0);
    \node[blue] at (2.5,1) {$y=\mathrm{arccsc}\,x$};
    \node at (1,-0.2) {$1$};
    \node at (-1,-0.2) {$-1$};
    \node at (0.2,1.57) {$\frac{\pi}{2}$};
    \node at (0.2,-1.57) {$-\frac{\pi}{2}$};
    \node at (0,-2.1) {(a) $y=\mathrm{arccsc}\,x$};

    % Additional dashed lines for special points
    \draw[dashed, gray] (-1,-1.7) -- (-1,1.7);
    \draw[dashed, gray] (1,-1.7) -- (1,1.7);
    \draw[dashed, gray] (-3.5,1.57) -- (3.5,1.57);
    \draw[dashed, gray] (-3.5,-1.57) -- (3.5,-1.57);
  \end{scope}

  %%%%%%%%%%%%%%%%%%%%%% arcsec(x) %%%%%%%%%%%%%%%%%%%%%%
  \begin{scope}[xshift=7.3cm]
    % Axes
    \draw[->] (-3.5,0) -- (3.5,0) node[right] {$x$};
    \draw[->] (0,-0.5) -- (0,3.5) node[above] {$y$};
    
    % arcsec(x) - red
    \draw[red, thick, smooth] plot coordinates {
      (-3.5,1.86) (-2,2.09) (-1,3.14) (-0.5,3.14)
      (0.5,1.05) (1,0) (2,1.05) (3.5,1.28)
    };
    
    % Discontinuity markers
    \draw[red, fill=white] (-1,3.14) circle (2pt);
    \draw[red, fill=white] (1,0) circle (2pt);
    
    % Labels
    \node[red] at (-2.5,2.5) {$y=\mathrm{arcsec}\,x$};
    \node at (1,-0.2) {$1$};
    \node at (-1,-0.2) {$-1$};
    \node at (0.2,3.14) {$\pi$};
    \node at (0.2,1.57) {$\frac{\pi}{2}$};
    \node at (0,-0.8) {(b) $y=\mathrm{arcsec}\,x$};

    % Additional dashed lines for special points
    \draw[dashed, gray] (-1,-0.5) -- (-1,3.5);
    \draw[dashed, gray] (1,-0.5) -- (1,3.5);
    \draw[dashed, gray] (-3.5,3.14) -- (3.5,3.14);
    \draw[dashed, gray] (-3.5,1.57) -- (3.5,1.57);
  \end{scope}

  %%%%%%%%%%%%%%%%%%%%%% arccot(x) %%%%%%%%%%%%%%%%%%%%%%
  \begin{scope}[xshift=14.1cm]
    % Axes
    \draw[->] (-3.5,0) -- (3.5,0) node[right] {$x$};
    \draw[->] (0,-0.5) -- (0,3.5) node[above] {$y$};
    
    % arccot(x) - green
    \draw[green!60!black, thick, smooth] plot coordinates {
      (-3.5,3.0) (-2,2.68) (-1,2.36) (0,1.57)
      (1,0.79) (2,0.46) (3.5,0.28)
    };
    
    % Asymptotes
    \draw[dashed] (-3.5,0) -- (3.5,0);
    \draw[dashed] (-3.5,3.14) -- (3.5,3.14);
    
    % Labels
    \node[green!60!black] at (2.5,2) {$y=\mathrm{arccot}\,x$};
    \node at (0.2,1.57) {$\frac{\pi}{2}$};
    \node at (0.2,3.14) {$\pi$};
    \node at (0,-0.8) {(c) $y=\mathrm{arccot}\,x$};

    % Additional dashed lines for special points
    \draw[dashed, gray] (0,1.57) -- (3.5,1.57);
    \draw[dashed, gray] (-3.5,2.36) -- (-1,2.36) -- (-1,0);
    \draw[dashed, gray] (1,0.79) -- (1,0);
  \end{scope}
\end{tikzpicture}
\end{document}
```

### Key Connections to Calculus
- **Derivatives**:
  - $\frac{d}{dx} e^x = e^x$
  - $\frac{d}{dx} \ln x = \frac{1}{x}$
  - $\frac{d}{dx} \sin x = \cos x$
- **Limits**:
  - $\lim_{x \to -\infty} e^x = 0$
  - $\lim_{x \to 0^+} \ln x = -\infty$


