# Matplotlib Important Methods with Examples

# What is Matplotlib?

Matplotlib is a Python library used for:

* Data Visualization
* Charts
* Graphs
* Plotting data

Import Matplotlib:

```python id="c6f1kp"
import matplotlib.pyplot as plt
```

---

# Basic Line Plot

```python id="a4x9md"
x = [1,2,3,4]
y = [10,20,30,40]

plt.plot(x, y)

plt.show()
```

---

# Important Plot Methods

---

# title()

Adds graph title.

```python id="u9q3ek"
plt.title("Sales Graph")
```

---

# xlabel()

X-axis label.

```python id="8k2vrf"
plt.xlabel("Months")
```

---

# ylabel()

Y-axis label.

```python id="o3x7tm"
plt.ylabel("Sales")
```

---

# legend()

Shows labels.

```python id="j7w2cl"
plt.plot(x, y, label="Sales")

plt.legend()
```

---

# grid()

Shows grid lines.

```python id="i4t8yn"
plt.grid()
```

---

# show()

Displays graph.

```python id="v0m2ra"
plt.show()
```

---

# Figure Size

```python id="y8n5fq"
plt.figure(figsize=(8,5))
```

---

# Line Customization

---

# color

```python id="r4w8zc"
plt.plot(x, y, color="red")
```

---

# linestyle

```python id="d5f1ou"
plt.plot(x, y, linestyle="--")
```

Styles:

* `-` solid
* `--` dashed
* `:` dotted

---

# linewidth

```python id="k2x9ve"
plt.plot(x, y, linewidth=3)
```

---

# marker

```python id="o9d3qt"
plt.plot(x, y, marker="o")
```

Markers:

* `o`
* `*`
* `s`
* `x`

---

# Complete Example

```python id="m7z1xp"
x = [1,2,3,4]
y = [10,20,30,40]

plt.figure(figsize=(6,4))

plt.plot(
    x,
    y,
    color="blue",
    linestyle="--",
    marker="o",
    label="Sales"
)

plt.title("Sales Data")

plt.xlabel("Months")
plt.ylabel("Sales")

plt.legend()

plt.grid()

plt.show()
```

---

# Bar Plot

Used for categorical data.

```python id="r8m4uk"
names = ["A", "B", "C"]
marks = [80, 90, 70]

plt.bar(names, marks)

plt.show()
```

---

# Horizontal Bar Plot

```python id="g2x5wn"
plt.barh(names, marks)
```

---

# Histogram

Shows frequency distribution.

```python id="l6v9pt"
data = [1,2,2,3,3,3,4,4,5]

plt.hist(data)

plt.show()
```

---

# Scatter Plot

Shows relation between variables.

```python id="c0q7ky"
x = [1,2,3,4]
y = [5,7,8,10]

plt.scatter(x, y)

plt.show()
```

---

# Pie Chart

```python id="q8f2dz"
labels = ["Python", "Java", "C++"]
sizes = [50, 30, 20]

plt.pie(sizes, labels=labels)

plt.show()
```

---

# explode in Pie Chart

Highlights section.

```python id="t3v8wn"
explode = [0.1, 0, 0]

plt.pie(sizes, labels=labels, explode=explode)
```

---

# Multiple Plots

```python id="d4k9yo"
x = [1,2,3]

y1 = [1,4,9]
y2 = [2,5,8]

plt.plot(x, y1, label="Square")
plt.plot(x, y2, label="Random")

plt.legend()

plt.show()
```

---

# subplot()

Multiple graphs in one figure.

```python id="b5n2vt"
plt.subplot(1,2,1)

plt.plot([1,2,3])

plt.subplot(1,2,2)

plt.plot([3,2,1])

plt.show()
```

Meaning:

* 1 row
* 2 columns
* 1st graph

---

# xlim() and ylim()

Set axis limits.

```python id="n1z6wc"
plt.xlim(0,10)

plt.ylim(0,50)
```

---

# xticks() and yticks()

Custom ticks.

```python id="s9f4rm"
plt.xticks([1,2,3,4])
```

---

# savefig()

Saves graph as image.

```python id="u3w8dx"
plt.savefig("graph.png")
```

---

# Style Sheets

```python id="p2m5cq"
plt.style.use("ggplot")
```

---

# Common Colors

```python id="y7d9ra"
red
blue
green
black
yellow
orange
purple
```

---

# Common Markers

| Marker | Shape    |
| ------ | -------- |
| o      | Circle   |
| *      | Star     |
| s      | Square   |
| x      | Cross    |
| ^      | Triangle |

---

# Common Line Styles

| Style | Meaning  |
| ----- | -------- |
| -     | Solid    |
| --    | Dashed   |
| :     | Dotted   |
| -.    | Dash Dot |

---

# Important Interview Notes

| Method    | Purpose      |
| --------- | ------------ |
| plot()    | Line graph   |
| bar()     | Bar graph    |
| hist()    | Histogram    |
| scatter() | Scatter plot |
| pie()     | Pie chart    |
| title()   | Graph title  |
| xlabel()  | X-axis label |
| ylabel()  | Y-axis label |
| legend()  | Show labels  |
| grid()    | Grid lines   |
| savefig() | Save graph   |

---

# Most Common Workflow

```python id="z8t2pn"
import matplotlib.pyplot as plt

x = [1,2,3,4]
y = [10,20,15,30]

plt.plot(x, y, marker="o")

plt.title("Simple Graph")

plt.xlabel("X values")
plt.ylabel("Y values")

plt.grid()

plt.show()
```

---
