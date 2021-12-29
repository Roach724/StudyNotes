# Lecture 1: Introduction

## Measure

Recall that on the real line $\mathcal{R}$, an interval such as $(a, b]$, we can define a length measure $\lambda$ such that the measure of the interval is given by $\lambda((a, b])=b-a$. Now we would like to expand this measure to all subsets of $\mathcal{R}$. Then we would like to require that such a measure $\lambda$ satisfies the following properties:

* (0) $\lambda$ is a mapping or function such that $\lambda$: $\mathcal{P}(\mathcal{R})\rightarrow \mathcal{R_+}\cup \{+\infty\}$ where $\mathcal{P}(\mathcal{R})$ is the power set of $\mathcal{R}$;
  
* (1) $\forall a,b \in \mathcal{R}, a<b$, $\lambda((a, b])=b-a$;

* (2) If $ A \subseteq \mathcal{R}, x \in \mathcal{R}$, define that $A+x=\{x+y, y\in A\}$. Then, $\forall A \subseteq \mathcal{R}, \forall x \in \mathcal{R}$, we have $\lambda(A+x)=\lambda(A)$. This is also known as **Translation Invariance**.

* (3) If $A=\bigcup_{j\geq1}A_j, A_i\cap A_j=\varnothing, i\neq j$, then $\lambda(A)=\sum_{j\geq1}\lambda(A_j)$, which is also known as $\sigma$-additive.

However, it is impossible to find such a measure that holding all the above properties. A paradox can be found if we try to do so by using the axiom of choice.

## Measure paradox: a non-measurable set

We first introduce the equivalence relation in $\mathcal{R}$. $\forall x, y\in \mathcal{R}$, we say that $x$ and $y$ are equivalent if $y-x \in \mathcal{Q}$ where $\mathcal{Q}$ is the set of all rational numbers. We denote this relation by $x\sim y$. Let $[x]=\{y\in \mathcal{R}, y-x\in \mathcal{Q}\}$ be the set of all real numbers that are equivalent to $x$, and define $\Lambda=\mathcal{R}|_\sim$ be the collection of all equivalent set in $\mathcal{R}$.