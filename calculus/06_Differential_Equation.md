# Differential Equations: Fundamental Concepts and Methods

## 1. Definition and Core Idea
A **differential equation (DE)** is an equation that relates an unknown function to its derivatives. It mathematically models how quantities change relative to other variables (e.g., time, space).

### General Form
An **n-th order ordinary differential equation (ODE)** is expressed as:
$$
F\left(x, y, \frac{dy}{dx}, \frac{d^2y}{dx^2}, \dots, \frac{d^ny}{dx^n}\right) = 0
$$
where:
- \( y = y(x) \) is the unknown function.
- \( \frac{d^ky}{dx^k} \) represents its \( k \)-th derivative.

## 2. Classification of Differential Equations

### 2.1 By Type
| Type                | Description                                                                 | Example                          |
|---------------------|-----------------------------------------------------------------------------|----------------------------------|
| **Ordinary DE (ODE)** | Contains derivatives with respect to **one** independent variable.          | \( \frac{dy}{dx} + 2y = e^x \)  |
| **Partial DE (PDE)**  | Contains partial derivatives with respect to **multiple** variables.        | \( \frac{\partial u}{\partial t} = k \frac{\partial^2 u}{\partial x^2} \) (Heat Equation) |

### 2.2 By Linearity
| Type          | Criteria                                                                 | Example                          |
|---------------|--------------------------------------------------------------------------|----------------------------------|
| **Linear**    | The unknown function and its derivatives appear linearly (no powers/products). | \( y'' + p(x)y' + q(x)y = r(x) \) |
| **Nonlinear** | Contains nonlinear terms (e.g., \( y^2 \), \( \sin(y) \), \( y \cdot y' \)). | \( y'' + y^3 = 0 \)              |

### 2.3 By Order
The **order** is the highest derivative present:
- **First-order**: \( \frac{dy}{dx} = f(x, y) \)
- **Second-order**: \( \frac{d^2y}{dx^2} + p(x)\frac{dy}{dx} = q(x) \)

---

## 3. Solutions of Differential Equations

### 3.1 Types of Solutions
| Solution Type   | Description                                                                 | Example                          |
|-----------------|-----------------------------------------------------------------------------|----------------------------------|
| **General Solution** | Contains arbitrary constants (equal to the order of the DE).                | \( y = Ce^{-2x} \) (for \( y' + 2y = 0 \)) |
| **Particular Solution** | Obtained by assigning specific values to constants (via initial/boundary conditions). | If \( y(0) = 3 \), then \( C = 3 \). |
| **Singular Solution**  | Solutions not obtainable from the general solution (rare).                  | Clairaut’s equation cases.       |

### 3.2 Existence and Uniqueness
For a first-order ODE \( y' = f(x, y) \) with initial condition \( y(x_0) = y_0 \):
- **Existence**: If \( f(x, y) \) is continuous near \( (x_0, y_0) \), a solution exists.
- **Uniqueness**: If \( f \) is Lipschitz in \( y \), the solution is unique.



## 4. Solution Methods for ODEs

### 4.1 First-Order ODEs
#### (a) Separable Equations
Form: \( \frac{dy}{dx} = f(x)g(y) \).  
**Solution**: Separate and integrate:
$$
\int \frac{dy}{g(y)} = \int f(x) \, dx + C
$$

**Example**:
$$
\frac{dy}{dx} = x y \implies \int \frac{dy}{y} = \int x \, dx \implies \ln|y| = \frac{x^2}{2} + C
$$

#### (b) Linear Equations
Form: \( \frac{dy}{dx} + P(x)y = Q(x) \).  
**Solution**: Use an **integrating factor（积分因子）** $\mu(x) = e^{\int P(x) dx}$:

##### Integrating Factor Method for First-Order Linear ODEs

**1. Standard Form**
First, ensure the equation is in standard form:

$$
\frac{dy}{dx} + P(x)y = Q(x)
$$

If not (e.g., the coefficient of $\frac{dy}{dx}$ is not 1), divide through by that coefficient.

**2. Compute the Integrating Factor $\mu(x)$**
The integrating factor is defined as:

$$
\mu(x) = e^{\int P(x) \, dx}
$$

**Key Points**:
- Omit the constant of integration $C$ since we only need one specific solution.
- The purpose of $\mu(x)$ is to transform the equation into an exact differential equation.

**3. Multiply by the Integrating Factor**
Multiply both sides by $\mu(x)$:

$$
\mu(x)\frac{dy}{dx} + \mu(x)P(x)y = \mu(x)Q(x)
$$

Using the product rule, the left side becomes:

$$
\frac{d}{dx}(\mu(x)y) = \mu(x)Q(x)
$$

**Derivation**:

$$
\frac{d}{dx}(\mu y) = \mu \frac{dy}{dx} + y \frac{d\mu}{dx}
$$
Since $\frac{d\mu}{dx} = \mu P(x)$ (because $\mu = e^{\int P(x) dx}$), substitution shows equivalence to the original equation.

**4. Integrate to Solve**
Integrate both sides:

$$
\mu(x)y = \int \mu(x)Q(x) \, dx + C
$$

The final solution is:

$$
y = \frac{1}{\mu(x)}\left(\int \mu(x)Q(x) \, dx + C\right)
$$

##### Worked Example

**Equation**:

$$
\frac{dy}{dx} + y = e^x
$$

**Step 1: Verify Standard Form**
The equation is already in standard form with:

$$
P(x) = 1,\quad Q(x) = e^x
$$

**Step 2: Compute Integrating Factor**

$$
\mu(x) = e^{\int P(x) dx} = e^{\int 1 \, dx} = e^x
$$

**Step 3: Multiply Through**

$$
e^x \frac{dy}{dx} + e^x y = e^x \cdot e^x = e^{2x}
$$

The left side becomes:

$$
\frac{d}{dx}(e^x y) = e^{2x}
$$

**Step 4: Integrate and Solve**

$$
e^x y = \int e^{2x} \, dx = \frac{1}{2}e^{2x} + C
$$

Divide both sides by $e^x$:

$$
y = \frac{1}{2}e^x + Ce^{-x}
$$

##### Example 2
We aim to solve:

$$
\frac{dy}{dx} = \frac{1}{x + y}
$$

using first-order linear equation methods.

**Rewrite the Equation**
First, observe that:

$$
\frac{dy}{dx} = \frac{1}{x + y}
$$

is not linear in $y(x)$. However, we can treat $x$ as a function of $y$.

**Invert the Relationship**
Take reciprocals to get:

$$
\frac{dx}{dy} = x + y
$$

which is linear in $x(y)$.

**Standard Linear Form**
Rewrite as:

$$
\frac{dx}{dy} - x = y
$$

This is now in the standard linear form:

$$
\frac{dx}{dy} + P(y)x = Q(y)
$$

where $P(y) = -1$ and $Q(y) = y$.

**Integrating Factor**
Compute the integrating factor:

$$
\mu(y) = e^{\int P(y) dy} = e^{\int -1 dy} = e^{-y}
$$

Multiply both sides by $\mu(y)$:

$$
e^{-y}\frac{dx}{dy} - e^{-y}x = ye^{-y}
$$

The left side is now an exact derivative:

$$
\frac{d}{dy}(xe^{-y}) = ye^{-y}
$$

Integrate with respect to $y$:

$$
xe^{-y} = \int ye^{-y} dy + C
$$

Using integration by parts:

$$
\int ye^{-y} dy = -ye^{-y} + \int e^{-y} dy = -ye^{-y} - e^{-y} + C
$$

Thus:

$$
xe^{-y} = -ye^{-y} - e^{-y} + C
$$

Multiply through by $e^y$:

$$
x = -y - 1 + Ce^y
$$

The implicit solution is:

$$
\boxed{x + y + 1 = Ce^y}
$$

##### Key Summary

1. **Applicability**: Only for first-order linear ODEs of the form $y' + P(x)y = Q(x)$.
2. **Integrating Factor**: $\mu(x) = e^{\int P(x) dx}$ (no constant needed).
3. **Transformation Trick**: Uses the product rule to get $\frac{d}{dx}(\mu y) = \mu Q(x)$.
4. **Solution Structure**: General solution = Particular solution (from $Q(x)$) + Homogeneous solution ($Ce^{-\int P(x) dx}$).

$$
y = \frac{1}{\mu(x)} \left( \int \mu(x) Q(x) \, dx + C \right)
$$

#### Solving First-Order Linear ODEs by Variation of Parameters

**1. Standard Form**
The standard form of a first-order linear differential equation is:

$$
\frac{dy}{dx} + P(x)y = Q(x) \quad (1)
$$

**2. Method of Variation of Parameters（常数变易法）**

**Step 1: Solve the Homogeneous Equation**
First solve the homogeneous version:

$$
\frac{dy}{dx} + P(x)y = 0 \quad (2)
$$

Using separation of variables:

$$
\begin{aligned}
\frac{dy}{y} &= -P(x)dx \\
\ln|y| &= -\int P(x)dx + C \\
y_h &= Ce^{-\int P(x)dx} \quad \text{(homogeneous solution)}
\end{aligned}
$$

**Step 2: Vary the Constant**
Replace the constant $C$ with a function $u(x)$:

$$
y_p = u(x)e^{-\int P(x)dx} \quad (3)
$$

**Step 3: Determine $u(x)$**
Substitute (3) into the non-homogeneous equation (1):

$$
\frac{d}{dx}\left[u(x)e^{-\int P(x)dx}\right] + P(x)u(x)e^{-\int P(x)dx} = Q(x)
$$

Expand the derivative:

$$
u'(x)e^{-\int P(x)dx} - u(x)P(x)e^{-\int P(x)dx} + P(x)u(x)e^{-\int P(x)dx} = Q(x)
$$

Simplifies to:

$$
u'(x)e^{-\int P(x)dx} = Q(x) \\
\Rightarrow u'(x) = Q(x)e^{\int P(x)dx}
$$

Integrate to find:

$$
u(x) = \int Q(x)e^{\int P(x)dx}dx + C
$$

**Step 4: General Solution**
Substitute back into (3):

$$
y = e^{-\int P(x)dx}\left(\int Q(x)e^{\int P(x)dx}dx + C\right)
$$

##### Worked Example
Solve:

$$
\frac{dy}{dx} + 2xy = x
$$

**Step 1: Homogeneous Solution**

$$
\frac{dy}{dx} + 2xy = 0 \\
\Rightarrow y_h = Ce^{-\int 2xdx} = Ce^{-x^2}
$$

**Step 2: Particular Solution Form**

$$
y_p = u(x)e^{-x^2}
$$

**Step 3: Find $u(x)$**
Substitute into original equation:

$$
u'(x)e^{-x^2} = x \\
\Rightarrow u'(x) = xe^{x^2} \\
\Rightarrow u(x) = \frac{1}{2}e^{x^2} + C
$$

**Step 4: Final Solution**

$$
y = e^{-x^2}\left(\frac{1}{2}e^{x^2} + C\right) = \frac{1}{2} + Ce^{-x^2}
$$



#### (c) Exact Equations
Form: \( M(x,y)dx + N(x,y)dy = 0 \), where \( \frac{\partial M}{\partial y} = \frac{\partial N}{\partial x} \).  
**Solution**: Find a potential function \( \psi(x,y) \) such that:
$$
\frac{\partial \psi}{\partial x} = M, \quad \frac{\partial \psi}{\partial y} = N
$$

#### (D) Homogeneous Differential Equations
##### 1. Definition and Identification
A **homogeneous differential equation** has the form:

$$
\frac{dy}{dx} = f\left(\frac{y}{x}\right)
$$

or equivalently:

$$
M(x,y)dx + N(x,y)dy = 0
$$

where $M(x,y)$ and $N(x,y)$ are homogeneous functions of the same degree (i.e., $M(tx,ty) = t^k M(x,y)$).

##### 2. Core Solution: Substitution Method
The key technique uses the substitution $v = \frac{y}{x}$ to convert the equation into separable form.

#### Step-by-Step Procedure:
1. **Substitution**:
   - Let $y = vx$, then by the product rule:

$$\frac{dy}{dx} = v + x\frac{dv}{dx}$$

2. **Transform the ODE**:
   - Substitute into $\frac{dy}{dx} = f\left(\frac{y}{x}\right)$:

$$v + x\frac{dv}{dx} = f(v)$$

   - Rearrange to separable form:

$$\frac{dv}{f(v) - v} = \frac{dx}{x}$$

3. **Integrate Both Sides**:

$$\int \frac{1}{f(v) - v} dv = \int \frac{1}{x} dx + C$$

4. **Back-Substitute**:
   - Solve for $v$, then replace $v = \frac{y}{x}$ to obtain the general solution.

#### 3. Worked Example
**Problem**: Solve $\frac{dy}{dx} = \frac{x^2 + y^2}{xy}$.

##### Solution:
1. **Rewrite in Homogeneous Form**:

$$\frac{dy}{dx} = \frac{y}{x} + \frac{x}{y} = v + \frac{1}{v} \quad \text{(where $v = y/x$)}$$

2. **Apply Substitution**:

$$v + x\frac{dv}{dx} = v + \frac{1}{v} \implies x\frac{dv}{dx} = \frac{1}{v}$$

3. **Separate and Integrate**:

$$\int v \, dv = \int \frac{1}{x} dx \implies \frac{v^2}{2} = \ln|x| + C$$

4. **Final Solution**:

$$\frac{y^2}{2x^2} = \ln|x| + C \implies y^2 = 2x^2\ln|x| + Cx^2$$


#### 4. Special Cases
##### Case 1: Non-Standard Homogeneous Form
For equations like:

$$\frac{dy}{dx} = f\left(\frac{ax + by + c}{dx + ey + f}\right)$$

- **If lines intersect**: Shift coordinates to the intersection point.
- **If lines are parallel**: Substitute $u = ax + by$.

##### Case 2: Implicit Homogeneity
Equations where homogeneity is not immediately obvious may require algebraic manipulation to identify the $y/x$ ratio.

##### Case 1: Shift to Intersection Point
**Applicable when**:  

$$\frac{dy}{dx} = \frac{a_1x + b_1y + c_1}{a_2x + b_2y + c_2}$$

where the lines intersect.

**Procedure**:
1. Find intersection point $(x_0,y_0)$ by solving:

$$\begin{cases}
a_1x + b_1y + c_1 = 0 \\
a_2x + b_2y + c_2 = 0
\end{cases}$$

2. Make substitution:

$$u = x - x_0, \quad v = y - y_0$$

3. Equation becomes homogeneous in $u$ and $v$.

**Example**:

$$\frac{dy}{dx} = \frac{2y-x+5}{2x-y-4}$$
- Intersection at $(1,-2)$
- Substitution: $u=x-1$, $v=y+2$
- Transformed equation:

$$\frac{dv}{du} = \frac{2v - u}{2u - v}$$

##### Case 2: Parallel Lines Substitution
**Applicable when**: 

$$\frac{dy}{dx} = f(ax + by + c)$$

**Procedure**:
1. Let $u = ax + by$
2. Compute $\frac{du}{dx} = a + b\frac{dy}{dx}$
3. Substitute to make separable.

**Example**:

$$\frac{dy}{dx} = \frac{y-2x+3}{y-2x+1}$$

- Let $u = y - 2x$
- Transformed equation:

$$\frac{du}{dx} = \frac{-u + 1}{u + 1}$$

##### Solution Table
| Case                  | Key Step                          | Resulting Form            |
|-----------------------|-----------------------------------|---------------------------|
| Intersecting lines    | Coordinate shift                 | Homogeneous in $u,v$      |
| Parallel lines        | $u = ax + by$ substitution       | Separable equation        |


**Important**: Always check if $\frac{M}{N}$ can be written as $F(\frac{y}{x})$ after manipulation.

#### 5. Bernoulli's Differential Equation:

##### 1. Definition
Bernoulli's equation is a special type of first-order nonlinear ordinary differential equation (ODE) with the form:

$$
\frac{dy}{dx} + P(x)y = Q(x)y^n \quad \text{where } n \neq 0,1
$$

Key characteristics:
- $P(x)$ and $Q(x)$ are known continuous functions
- $n$ is a real constant (nonlinear when $n \neq 0,1$)
- Becomes linear when $n=0$ or separable when $n=1$

##### 2. Solution Method (Variable Substitution)

**Step 1: Standard Form**
Ensure the equation matches the standard Bernoulli form:

$$
y' + P(x)y = Q(x)y^n
$$

**Step 2: Variable Substitution**
Introduce a new variable:

$$
v = y^{1-n}
$$

Its derivative relates to the original equation:

$$
\frac{dv}{dx} = (1-n)y^{-n}\frac{dy}{dx}
$$

**Step 3: Equation Transformation**
Multiply the original equation by $(1-n)y^{-n}$:

$$
(1-n)y^{-n}y' + (1-n)P(x)y^{1-n} = (1-n)Q(x)
$$

Substitute $v$ and its derivative:

$$
\frac{dv}{dx} + (1-n)P(x)v = (1-n)Q(x)
$$

**Step 4: Solve the Linear Equation**
The transformed linear equation in $v$:

$$
\frac{dv}{dx} + \tilde{P}(x)v = \tilde{Q}(x)
$$

where:
- $\tilde{P}(x) = (1-n)P(x)$
- $\tilde{Q}(x) = (1-n)Q(x)$

Solve using integrating factor method.

**Step 5: Back-Substitution**
After finding $v(x)$, return to the original variable:

$$
y = v^{1/(1-n)}
$$

##### 3. Worked Example
Solve:
$$
\frac{dy}{dx} + \frac{y}{x} = x^2y^3
$$

- $P(x) = \frac{1}{x}$
- $Q(x) = x^2$
- $n = 3$

Let $v = y^{-2}$ ⇒ $\frac{dv}{dx} = -2y^{-3}\frac{dy}{dx}$

Multiply by $-2y^{-3}$:

$$
-2y^{-3}y' - \frac{2}{x}y^{-2} = -2x^2
$$

Substitute $v$:

$$
\frac{dv}{dx} - \frac{2}{x}v = -2x^2
$$

Integrating factor:

$$
\mu(x) = e^{\int -\frac{2}{x}dx} = x^{-2}
$$

Solution:

$$
v = x^2\left(\int -2x^2 \cdot x^{-2} dx + C\right) = x^2(-2x + C)
$$

##### Final Solution

$$
y = \pm \frac{1}{\sqrt{Cx^2 - 2x^3}}
$$

**Note**: This method extends the separation of variables technique to a broader class of nonlinear ODEs.

### 4.2 Second-Order Linear ODEs

**General form**:
  
$$
y'' + p(x)y' + q(x)y = r(x)
$$


#### (a) Homogeneous Case ($r(x) = 0$)

For constant-coefficient ODEs of the form:  

$$
y'' + a y' + b y = 0
$$

1. **Characteristic Equation**:  
   Solve the quadratic:

$$
r^2 + a r + b = 0
$$

2. **Solution Types**:

**i. Real distinct roots** $r_1 \neq r_2$:

$$
\boxed{y = C_1 e^{r_1 x} + C_2 e^{r_2 x}}
$$

   - **Example**:  
  $y'' - 3y' + 2y = 0$  
  Characteristic equation: $r^2 - 3r + 2 = 0 \Rightarrow r = 1, 2$  
  Solution:  

$$
y = C_1 e^x + C_2 e^{2x}
$$

**ii. Repeated root** $r$:

$$
\boxed{y = (C_1 + C_2 x) e^{r x}}
$$

  **Example**:  
  $y'' - 4y' + 4y = 0$  
  Characteristic equation: $r^2 - 4r + 4 = 0 \Rightarrow r = 2$  
  Solution:  

$$
y = (C_1 + C_2 x) e^{2x}
$$

**iii. Complex conjugate roots** $r = \alpha \pm \beta i$:

$$
\boxed{y = e^{\alpha x} (C_1 \cos \beta x + C_2 \sin \beta x)}
$$

  **Example**:  
  $y'' + y = 0$  
  Characteristic equation: $r^2 + 1 = 0 \Rightarrow r = \pm i$  
  Solution:  

$$
y = C_1 \cos x + C_2 \sin x
$$


#### (b) Nonhomogeneous Case ($r(x) \neq 0$)

- **General Solution**: 

$$
y = y_h + y_p
$$

  where:
  - $y_h$ is the **complementary (homogeneous)** solution.
  - $y_p$ is a **particular solution**, found via:
    - **Undetermined Coefficients** (for simple $r(x)$ like exponentials, polynomials, sines/cosines)
    - **Variation of Parameters** (for general $r(x)$)

**Example**:  
Solve  

$$
y'' - 3y' + 2y = e^x
$$

- Step 1: Solve the homogeneous equation $y'' - 3y' + 2y = 0$  
  ⇒ $y_h = C_1 e^x + C_2 e^{2x}$

- Step 2: Guess particular solution: $y_p = A x e^x$  
  ⇒ Plug into original equation and solve for $A$

- Final general solution:  

$$
y = C_1 e^x + C_2 e^{2x} + A x e^x
$$
