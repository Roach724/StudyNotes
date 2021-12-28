# Notes of Lecture3: Set Functions

## Measure continouity

We start by a set of definitions.

**DEFINITION** Let $\mathcal{C} \subseteq \mathcal{S}(\Omega)$, where $\mathcal{S}(\Omega)$ denote a collection of subests of $\Omega$, define a measure $\mu$ on $\mathcal{C}$ whose values are on $\mathbb{R}_+ + \{+\infty\}$.

* $\forall E \in \mathcal{C}$, $\mu$ is said to be continous form below at $E$, if $\forall (E_n)_{n \geq1}, E_n \in \mathcal{C}, E_n \subseteq E_{n+1}, \bigcup_{n \geq 1} E_n = E, s.t. \lim_{n \to +\infty}\mu(E_n) = \mu(E)$, where the conditions satisfied by $E_n$ is denoted by $E_n \uparrow E$.

* $\forall E \in \mathcal{C}$, $\mu$ is said to be continous form above at $E$, if $\forall (E_n)_{n \geq1}, E_n \in \mathcal{C}, E_n \supseteq E_{n+1}, \exists \eta_0, \mu(E_{\eta_0})<\infty, \bigcap_{n \geq 1} E_n = E, s.t. \lim_{n \to +\infty}\mu(E_n) = \mu(E)$, where the conditions satisfied by $E_n$ is denoted by $E_n \downarrow E$.

* $\mu$ is said to be continous at $E$ if and only if $\mu$ is both continous from above and below at $E$.

**LEMMA** Let $a$ be an algebra and $a \subseteq \mathcal{S}(\Omega)$, measure $\mu$ is defined on $a$ whose values are on $\mathbb{R}_+ + \{+\infty\}$ and assuming that $\mu$ is additive. We have the following conclusions:

* (1) $\mu$ is $\sigma$-additive $\Rightarrow$ $\forall E \in a$, $\mu$ is continous at $E$.

* (2) $\mu$ is continous from below $\Rightarrow$ $\mu$ is $\sigma$-additive.

* (3) $\mu$ is continous from above at $\varnothing$ and $\mu$ is finite $\Rightarrow$ $\mu$ is $\sigma$-additive.

$PROOF$

* (1.1) We first prove that $\mu$ is $\sigma$-additive $\Rightarrow$ $\mu$ is continous from below $\forall E \in a$. Suppose $E \in a$ and a sequence of sets $E_n \uparrow E$. Since $E_n$ is increasing, we construct a new sequence $\{F_n\}$ based on $\{E_n\}$ where $F_n = E_n|E_{n-1}$ and $E_0=\varnothing$. Hence, $F_n 's$ are disjoint pairwise i.e. $F_i \cap F_j = \varnothing, i \neq j$. It is obvious that $\bigcup_{i\geq1}^{n}F_i=\bigcup_{i\geq1}^{n}E_i$ and $\sum_{i=1}^{n} F_i = E_n$. Since $\mu$ is $\sigma$ additive, $\mu(E)=\sum\mu(E_i)=\sum\mu(F_i)=\lim_{n\to \infty} \sum_{i=1}^{n}\mu(F_i)=\lim_{n\to \infty}\mu(\sum_{i=1}^{n}F_i) = \lim_{n \to \infty} \mu(E_n)$. This proves that $\mu$ is continous from below at any $E\in a$.

* (1.2) Now we prove that $\mu$ is continous from above. Suppose $E \in a$ and a sequence of sets $E_n \downarrow E$ where $\exist n_0 $, $s.t. \forall n > n_0, \mu(E_n) < \infty$. Considering the following set sequence $G_n$ where $G_1 = E_{n_0}|E_{n_0 + 1}, ... , G_n = E_{n_0}|E_{n_0+n}$, $E_n$ is decreasing thus $G_n$ is increasing and $G_n \uparrow E_{n_0}|E$. Since all $E_n 's$ are in the algebra $a$, then $G_n \in a$. By the conclusion we draw on (1), we have that $\lim_{n \to \infty}\mu(G_n)=\mu(E_{n_0}|E)$. Since $E\subseteq E_n$. Then $$\mu(E_{n_0})-\mu(E)=\mu(E_{n_0}|E)=\lim_{n \to \infty}\mu(G_n)=\lim_{n \to \infty}(\mu(E_{n_0})-\mu(E_{n_0+n}))=\mu(E_{n_0})-\lim_{n \to \infty}\mu(E_{n_0+n})$$, which leads to $\mu(E)=\lim_{n \to \infty}\mu(E_{n_0+n})$. This proves that $\mu$ is continous from above. Thus we concludes the proof. *The statement here is not as useful as the statements below because we it is derived from $\mu$ is $\sigma$-additive. In reality, we usually don't have any idea if a measure $\mu$ is $\sigma$ additive and instead we usually do the opposite: prove that a mearsure is $\sigma$-additive.*
  
* (2) Assume that a measure $\mu$ is continous from below and $E=\sum_{k\geq 1}E_k, E, E_k \in a, E_i \cap E_j = \varnothing, i \neq j$. We know that $\forall n \geq 1, \sum_{k=1}^{n}E_k\subseteq E$, thus $\mu(\sum_{k=1}^{n}E_k) \leq \mu(E)$. Since $\mu$ is additive then we have $\sum_{k=1}^{n}\mu(E_k)\leq \mu(E)$. By the limit inequality, $lim_{n \to \infty}\sum_{k=1}^{n}\mu(E_k)=\sum_{k\geq1}\mu(E_k)\leq \mu(E)$. Let $F_n = \sum_{k=1}^{n}E_k \in a$, thus $F_n \uparrow E$. Since $\mu$ is  continous from below, thus $$\lim_{n \to \infty} \mu(F_n) = \lim_{n \to \infty} \sum_{k=1}^{n}\mu(E_k)=\sum_{k\geq1}\mu(E_k)=\mu(E).$$ This proves that $\mu$ is $\sigma$ additive.

* (3) Suppose that $\mu$ is continous from above at $\varnothing$ and $\mu(\Omega) < \infty$. Let $E, E_k \in a, E=\sum_{k \geq1}E_k$, then $F_n=\sum_{k\geq n}E_k \in a$, thus $F_n=(E|\sum_{j=1}^{n-1}E_j)$ and it is obvious that $F_n \downarrow \varnothing$, we also have that $\mu(F_1)<\infty$. By the continouity above $\varnothing$, then $\mu(F_n) \rightarrow \mu(\varnothing)=0$. Then $\mu(E)=\mu(\sum_{k=1}^{n}\cup \sum_{k\geq n}E_k)=\sum_{i=1}^{n}\mu{E_k}+\mu(F_{n+1})$. By taking the limit on both side of the equation, we hanve $\mu(E)=\mu(\sum_{k\geq1}E_k) = \sum_{k\geq1}\mu(E_k)+0=\sum_{k\geq1}\mu(E_k)$, this proves that $\mu$ is $\sigma$-additive. Thus we conclude the lemma. $\square$

**EXAMPLE** Suppose $\Omega=(0, 1)$ and $\mathcal{C}$ be the collection of intervals in which the intervals has the form of $(a,b], 0\leq a<b<1$. Define the measure $\mu$ to be as follow: $$\mu((a,b])=\begin{cases}
 & b-a,\text{ if } a>0 \\
 & +\infty,\text{ if } a=0
\end{cases}.$$

Suppose $E_1=(a_1, b_1]\in \mathcal{C}, E_2=(a_2, b_2] \in \mathcal{C}, E_1\cap E_2=\varnothing$, where $a_1, a_2$ are not zero, then by definition of $\mu$, we have $\mu(E_1\cup E_2)=b_1-a_1+b_2-a_2=\mu((a_1, b_1])+\mu((a_2, b_2])$, the same conclusion holds for $a_1, a_2$ are 0. Thus $\mu$ is additive. However, $\mu$ is *NOT* $\sigma$-additive. $\square$

## Extension of measure

**Theorem 1** Suppose $\mathcal{F} \subseteq \mathcal{\Omega}$ be a semi-algebra and $\mu$ be a additive measure defined on $\mathcal{F}$. Now we show that there exists a extension measure $\nu$, s.t. (1) $\nu$ is a measure defined on the algebra generated by $\mathcal{F}$, which is denoted by $a(\mathcal{F})$; (2) $\forall A \in \mathcal{F}, \nu(A)=\mu(A)$; (3) if $\mu_1, \mu_2$ are defined on $a(\mathcal{F})$, then $\forall A \in \mathcal{F}, \mu_1(A)=\mu_2(A)$ implies $\mu_1(E)=\mu_2(E), \forall E\in a(\mathcal{F})$

$PROOF$ Recall the important property of an algebra generated by a semi-algabra： $A\in a(\mathcal{F})$ implies that there exists a finite sequence $E_i,s.t. A=\sum_{i=1}^{n}E_i, E_i \in \mathcal{F}$. Then we propose $$\nu(A)=\sum_{j=1}^{n}\mu(E_j).$$ Next we prove the following properties that $\nu$ has: (1) $\nu$ is well-define;(2) $\nu$ is additive;(3) the uniqueness of $\nu$.

* (1) Assume that $A=\sum_{i=1}^{m}F_k$, then we want to show $\nu(A)=\sum_{j=1}^{n}\mu(E_j)=\sum_{k=1}^{m}\mu(F_k)$. We know that $E_j \subseteq A = \sum_{k=1}^{m}F_k$, thus $E_j=E_j\cap \sum_{k=1}^{m}F_k = \sum_{k=1}^{m} E_j \cap F_k$, by the property of semi-algebra the element $E_j \cap F_k \in \mathcal{F}$. By additivity of semi-algebra, we have $$\mu(E_j)=\mu(\sum_{k=1}^{m} E_j \cap F_k)$$. Therefore,$\nu(A)=\sum_{j=1}^{n}\mu(E_j)=\sum_{j=1}^{n}\sum_{k=1}^{m}\mu(E_j \cap F_k)$. The same argument holds for $\nu(A)=\sum_{k=1}^{m}\mu(F_k)$ and hence $\nu$ is well define.

* (2) We next prove the additivity of $\nu$. Let $B=\sum_{k=1}^{m}F_k$ where $A\cap B=\varnothing, F_k \in \mathcal{F}$. Thus $A \cup B=\sum_{j=1}^{n}E_j+\sum_{k=1}^{m}F_k$. Thus, by definition of a semi-algebra, $\nu(A\cup B)=\sum_{j=1}^{n}\mu(E_j)+\sum_{k=1}^{m}\mu(F_k)=\nu(A)+\nu(B)$. This shows that $\nu$ is additive.

* (3) Now we show the uniqueness. We would like to show that for $\mu_1, \mu_2$ define on $a(\mathcal{F})$ and $\mu_1(A)=\mu_2(A),\forall A\in \mathcal{F}$ and $\mu_1, \mu_2$ are additive, $\mu_1(B)=\mu_2(B), \forall B \in a(\mathcal{F})$. Let $B \in a(\mathcal{F})$, then $B=\sum_{j=1}^{n}E_j, E_j\in \mathcal{F}$, then $\mu_1(B)=\sum_{j=1}^{n}\mu_1(E_j)=\sum_{j=1}^{n}\mu_2(E_j)=\mu_2(B)$. This proves the uniqueness. $\square$

We now show that if $\mu$ is $\sigma$-additive then $\nu$ is also $\sigma$-additive.

$PROOF$
Suppose $A=\sum_{k\geq1}A_j$ where $A, A_j \in a(\mathcal{F})$, we would like to show that $\nu(A)=\sum_{k\geq1}\nu(A_k)$. Since $A\in a(\mathcal{F})$, then $A=\sum_{j=1}^{n}E_j, E_j\in \mathcal{F}$. In addition, each $A_k \in a(\mathcal{F})$, thus $A_k=\sum_{l=1}^{n_k}E_{k,l}, E_{k,l} \in \mathcal{F}$. By definition, we have $\nu(A)=\sum_{j=1}^{n}\mu(E_j)$. Observe that $E_j=E_j\cap A=E_j \cap (\sum_{k\geq1}A_k)=E_j\cap (\sum_{k\geq1}\sum_{l=1}^{n_k}E_{k,l})=\sum_{k\geq1}\sum_{l=1}^{n_k}E_{k,l}\cap E_j$. Since $\mu$ is $\sigma$-additive, $\mu(E_j)=\sum_{k\geq1}\sum_{l=1}^{n_k}\mu(E_{k,l}\cap E_j)$. Hence $\nu(A)=\sum_{j=1}^{n}\sum_{k\geq1}\sum_{l=1}^{n_k}\mu(E_{k,l}\cap E_j)$. Moreover, $E_{k,l}=A\cap E_{k,l}=\sum_{j=1}^{n}E_{k,l}\cap E_j$, then $\mu(E_{k,l})=\sum_{j=1}^{n}\mu(E_{k,l}\cap E_j)$. Recall that $\nu(A_k)=\sum_{l=1}^{n_k}\mu(E_{k,l})$, thus $\sum_{k\geq1}\nu(A_k)=\sum_{k\geq1}\sum_{l=1}^{n_k}\mu(E_{k,l})=\sum_{k\geq1}\sum_{l=1}^{n_k}\sum_{j=1}^{n}\mu(E_{k,l}\cap E_j)=\sum_{j=1}^{n}\sum_{k\geq1}\sum_{l=1}^{n_k}\mu(E_{k,l}\cap E_j)=\nu(A)$. Therefore, $\nu(A)=\sum_{k\geq1}\nu(A_k)$, this proves that the extension $\nu$ is also $\sigma$-additive. $\square$
