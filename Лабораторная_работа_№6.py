{
  "nbformat": 4,
  "nbformat_minor": 0,
  "metadata": {
    "colab": {
      "provenance": [],
      "collapsed_sections": [],
      "authorship_tag": "ABX9TyPzz6WD0oOs2b8kEf81P3+m",
      "include_colab_link": true
    },
    "kernelspec": {
      "name": "python3",
      "display_name": "Python 3"
    },
    "language_info": {
      "name": "python"
    }
  },
  "cells": [
    {
      "cell_type": "markdown",
      "metadata": {
        "id": "view-in-github",
        "colab_type": "text"
      },
      "source": [
        "<a href=\"https://colab.research.google.com/github/Od1nsky/Kapustian-VS-PI-311/blob/main/%D0%9B%D0%B0%D0%B1%D0%BE%D1%80%D0%B0%D1%82%D0%BE%D1%80%D0%BD%D0%B0%D1%8F_%D1%80%D0%B0%D0%B1%D0%BE%D1%82%D0%B0_%E2%84%966.py\" target=\"_parent\"><img src=\"https://colab.research.google.com/assets/colab-badge.svg\" alt=\"Open In Colab\"/></a>"
      ]
    },
    {
      "cell_type": "code",
      "execution_count": null,
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/",
          "height": 562
        },
        "id": "oUElM4xfX2sG",
        "outputId": "b6af5b55-b4da-4779-e8ea-7661d25f8194"
      },
      "outputs": [
        {
          "output_type": "display_data",
          "data": {
            "text/plain": [
              "<Figure size 750x400 with 1 Axes>"
            ],
            "image/png": "iVBORw0KGgoAAAANSUhEUgAAAmsAAAFLCAYAAACJCMtPAAAABHNCSVQICAgIfAhkiAAAAAlwSFlzAAAHsAAAB7AB1IKDYgAAADh0RVh0U29mdHdhcmUAbWF0cGxvdGxpYiB2ZXJzaW9uMy4yLjIsIGh0dHA6Ly9tYXRwbG90bGliLm9yZy+WH4yJAAAW/UlEQVR4nO3df6zddZ3n8ddHig5Fp1RLu4EWsTqbWVJbfuysxh8Rs04xMGscIGMUQwRFKhQqhSqsP/Yi44yzKMivwiCb9RfNrKLbFWHC6CYQEsUfEbS3pNmJSCkyaalInUJH0PvZP85pKeVW6LftOZ977+ORkN57es49b94pp0++55zvKbXWAADQphcNewAAAHZPrAEANEysAQA0bNqwB0iSk08+uR5yyCE55JBDhj3KhPX444/bX0d2153ddWd33dldd3bX3SB3d+WVV36z1nrK9u+biLUjjzwyZ555ZhYsWDDsUSas0dFR++vI7rqzu+7srju7687uuhvk7q688sr1O3/vaVAAgIaJNQCAhjXxNOiutmzZki1btqSUMuxRJowDDjggGzZs6HTbWmtmzJiRGTNm7OOpAIC91WyszZs3T6ztgW3btuWggw7qdNtaazZs2CDWAKBBTT4NWkoRagNk3wDQriZjDQCAniafBn0hxupY5l81P+u3rM/GizZm9sGzn/c2X/ziF3PLLbfkiCOOyIEHHpirrrpqAJMCAHQ3YY+snXjziVm/ZX0Of9nhLyjUtluyZElWrlyZX/3qV0mSFStW5Mc//nEuvfTS3HXXXbnnnnty+umn5/TTT88999yTJBkZGcnZZ5+dN77xjXnwwQczMjKS0dHRJMmpp576rF+TXhR++9vfzr333ptly5bl3HPPzVe/+tVnzXHJJZfknHPOyXXXXZcHH3wwF1100Y77Gh0dzW233ZaPfOQjed/73pfHHntsx+Xr1q3LyMhItmzZkg9/+MNZtmxZPv7xjz9rhu33v/023/jGN/K6170uSXLhhRdmxYoVWbRoUbZu3brHewcABmvCxtr8mfOTJLefdvse3e4LX/hCPvCBD2TmzJlJkssuuyyf+MQn8rvf/S5vectbcs011+TGG2/MjTfemOuuuy5JsnXr1lx88cV585vfvOPnrFy5MiMjI3n88ceTJPfff38+9rGP5corr9xxnSuuuCIzZ87MoYcemnvvvfdZc7zrXe/K+vXrM3369CTJ9773vYyMjOTOO+9M0nt359jYWJ5++ul897vfzcEHH/ysuFq1alW2bduWmTNn5oEHHshTTz2V+++/PyMjI1m9evWO622//bx585Ikv/jFL3L55ZfnmGOO2aO9AQDDMWFjbe2ja7NozqIsnLNwj2531lln5aabbsphhx2Wn/70p9m6dWumTZu2I4RqrTtecF9rTZI88sgjOeyww571c84555yMjIzs+OiJo446Kp/+9Kfzgx/8INu2bUuSPPXUU1m2bFlGRkbyuc997lm3P/roo/Otb30rP/zhD5Mkb3jDGzIyMpLjjz8+SXL99dfns5/9bBYvXpwnn3wy7373u7Nq1apce+21SZKxsbGcdNJJGRkZyapVq/LiF784Rx11VEZGRvLOd75zx/1cf/31WbJkyY7v3/a2t+WUU07Jfffdt0d7AwCGY8LG2satG3P2cWfv8e1uuOGGnHfeeVmzZk1e/epXZ8WKFbn++uszf/78rF69OkuXLs2SJUuyZMmSnHPOObntttvyox/9KJdddlnuvvvufP/73x/3565duzYXX3xxpk+fvuMUGh/96Edz3nnn5cILL8w111yz47qPPfZYLrjggpxxxhl5zWteM+7P2x5/3/nOd5Ikc+fOzdVXX52lS5cmSd773vfm61//elasWJFly5bt9t93bGwsixYtStI7ynb//ffnhhtuyNFHH73HuwOAqWisjuWmn9yUcmnJpic2Dfz+y/ajR8O0fPnyuvNng27YsGHH03bD9qlPfSqf/OQnd3x/9dVX5/zzzx/iROPbm/OsJW3tfNB8Vl53dted3XVnd93ZXTdv/+rbc9i2w/JP//pPeXj5w/v9/kopV9Zal2//vskja7XWtBCRSZ4VakmaDLW91dK+AaA1XV8nv680eeqOGTNmZMOGDU7Uuge2bt2al770pZ1uu/3jpgCA51r76Nq8fvrr9/h18vtKs7EmHvbM6OjolH0aEwD2p41bN2bhnw4n1JJGnwYFAGjFuqXrsujfLRra/Ys1AICGiTUAgIaJNQCAhok1AICGiTUAgIaJNQCAhok1AICGiTUAgIaJNQCAhok1AICGiTUAgIaJNQCAhok1AICGiTUAgIaJNQCAhok1AICGiTUAgIaJNQCAhok1AICGiTUAgIaJNQCAhok1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\n"
          },
          "metadata": {
            "needs_background": "light"
          }
        },
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "цельсия[-67.0]= фаренгейт [-88.6]\n",
            "цельсия[-34.0]= фаренгейт [-29.2]\n",
            "цельсия[0]= фаренгейт [32.0]\n",
            "цельсия[54.0]= фаренгейт [93.2]\n",
            "цельсия[100]= фаренгейт [129.2]\n",
            "цельсия [-50] фаренгейта [-51.57743455]\n",
            "цельсия [10] фаренгейта [26.53883728]\n",
            "цельсия [30] фаренгейта [52.57759456]\n",
            "цельсия [20] фаренгейта [39.55821592]\n",
            "цельсия [10] фаренгейта [26.53883728]\n",
            "цельсия [70] фаренгейта [104.65510912]\n",
            "цельсия [87] фаренгейта [126.7880528]\n"
          ]
        }
      ],
      "source": [
        "import matplotlib.pyplot as plt\n",
        "\n",
        "\n",
        "celsius = [[-67.0], [-34.0], [0], [54.0], [100]]\n",
        "farenheit = [[-88.6], [-29.2], [32.0],[93.2],[129.2]]\n",
        "\n",
        "import numpy as np\n",
        "\n",
        "x_range = np.arange(-70, 120)\n",
        "y_range = x_range*1.8+32\n",
        "\n",
        "plt.figure(figsize=(15,8), dpi=50)\n",
        "plt.scatter(celsius, farenheit, label=\"Входные значения\", color=\"green\", marker=\"$f$\")\n",
        "plt.xlabel(\"celsius\")\n",
        "plt.ylabel(\"farenheit\")\n",
        "plt.legend()\n",
        "plt.grid(True)\n",
        "plt.show()\n",
        "\n",
        "for c,f in zip(celsius, farenheit):\n",
        "  print(f\"цельсия{c}= фаренгейт {f}\")\n",
        "\n",
        "from sklearn.linear_model import LinearRegression\n",
        "\n",
        "lr = LinearRegression()\n",
        "lr.fit(celsius, farenheit)\n",
        "lr.predict([[256], [123]])\n",
        "lr.coef_\n",
        "lr.intercept_\n",
        "celsius_test = [[-50], [10], [30], [20], [10], [70], [87]]\n",
        "farenheit_test = lr.predict(celsius_test)\n",
        "farenheit_test\n",
        "\n",
        "for c,f in zip(celsius_test, farenheit_test):\n",
        "  print(f\"цельсия {c} фаренгейта {f}\" )\n",
        "\n"
      ]
    },
    {
      "cell_type": "markdown",
      "source": [
        "Задания обычной сложности"
      ],
      "metadata": {
        "id": "D9D6hc9JfxR7"
      }
    },
    {
      "cell_type": "markdown",
      "source": [
        "Задание 1"
      ],
      "metadata": {
        "id": "CZHN35aIlGjf"
      }
    },
    {
      "cell_type": "code",
      "source": [
        "import matplotlib.pyplot as plt\n",
        "\n",
        "farenheit = [[0], [10],[20], [30]]\n",
        "kelvin = [[255.372], [260.928], [266.483], [272.039]]\n",
        "\n",
        "import numpy as np\n",
        "\n",
        "x_range = np.arange(-70, 120)\n",
        "y_range = x_range*1.8+32\n",
        "\n",
        "plt.figure(figsize=(15,8), dpi=50)\n",
        "plt.scatter(farenheit, kelvin, label=\"Входные значения\", color=\"green\", marker=\"$f$\")\n",
        "plt.xlabel(\"farenheit\")\n",
        "plt.ylabel(\"kelvin\")\n",
        "plt.legend()\n",
        "plt.grid(True)\n",
        "plt.show()\n",
        "\n",
        "for c,f in zip(farenheit, kelvin):\n",
        "  print(f\"фаренгейт{c}= кельвин{f}\")\n",
        "\n",
        "from sklearn.linear_model import LinearRegression\n",
        "\n",
        "lr = LinearRegression()\n",
        "lr.fit(farenheit, kelvin)\n",
        "lr.predict([[256], [123]])\n",
        "lr.coef_\n",
        "lr.intercept_\n",
        "farenheit_test = [[-50], [10], [30], [20], [10], [70], [87]]\n",
        "kelvin_test = lr.predict(celsius_test)\n",
        "print(kelvin_test)\n",
        "\n",
        "for c,f in zip(farenheit_test, kelvin_test):\n",
        "  print(f\"фаренгейта {c} кельвина {f}\" )\n",
        "\n",
        "\n"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/",
          "height": 654
        },
        "id": "uaruFSgrfw5Y",
        "outputId": "9816c10a-2a91-4bf2-8959-3570441c1689"
      },
      "execution_count": null,
      "outputs": [
        {
          "output_type": "display_data",
          "data": {
            "text/plain": [
              "<Figure size 750x400 with 1 Axes>"
            ],
            "image/png": "iVBORw0KGgoAAAANSUhEUgAAAnEAAAFLCAYAAAC5hNpuAAAABHNCSVQICAgIfAhkiAAAAAlwSFlzAAAHsAAAB7AB1IKDYgAAADh0RVh0U29mdHdhcmUAbWF0cGxvdGxpYiB2ZXJzaW9uMy4yLjIsIGh0dHA6Ly9tYXRwbG90bGliLm9yZy+WH4yJAAAcLElEQVR4nO3de5CddZ3n8fdXAkK4GQxBE0AIlKVMkzCuqOOlvGy245LRCbdBhCAIDgESYhrCZchYjeCIDoQhCvGSDLhgalkWK8MIqaiDqFOKSoUAJ4hu1UomGCuhDRc7gED6u3+ck9j0JqHTJ08ffn3er6rUOf08z+/5ffPNqc6nntuJzESSJElleV2rC5AkSdLOM8RJkiQVyBAnSZJUoFGtLmBHTjjhhDzssMMqn+fpp5/mDW94Q+XztCv7Wy37Wy37Wy37Wz17XK3h6u/111//ncw8sf+y13SIO+yww1iwYEHl89RqNTo6Oiqfp13Z32rZ32rZ32rZ3+rZ42oNV3+vv/76NQOXeTpVkiSpQIY4SZKkAr2mT6f299xzz7Fx40aqeK7dbrvtxtq1a3f5fksXERxwwAGMHj261aVIkqQBmgpxETEdmAbsBywBTmismtJY/gHgXcABwNWZuarf2OXAGqA3My9+tbl6enqYMGECu+22WzMlb9Pzzz/PXnvttcv3W7rNmzfzu9/9jkMPPbTVpUiSpAGaCnGZuQxYFhFjgGsz8+yI2AO4IzN/DfwaWBwRfwl8DFjVb/hz1E/nrh+434iYCkzt7OykVqsB9aNlL774YjPlbtfLL7/M888/X8m+S7dp06at/wZD1dPT0/Q+tH32t1r2t1r2t3r2uFqt7O+uOp06H7ix8X468K9bVkTEKOBC4HMDxpycmX0RsSAiJmXmw1tWZOYKYEVXV9fcLXd8rF27trKjZR6J27599tmHQw45pKl9eGdUtexvtexvtexv9exxtVrZ32ZPpwZwDbA8M1c2Fn8CmNFYvzv1cPfPmfmKi84ys6/xdgOwTzN1bNGXfUy8YSJrnlnD+ovXM27vca865pZbbuH222/n8MMPZ/fdd+eGG27YFaVIkiRVqtm7U2dTv/7tpIiYGRETgQ2Zuamx/kvAW4HzIuJkgIi4tfH6rYhYBBwB3N9kHQAc9+3jWPPMGibsO2FQAW6Lc845h5tuuok//OEPAMybN48HHniAK6+8kh/96Efcf//9nHHGGZxxxhncf3+91O7ubs4991ze97738fjjj9Pd3b31cOpJJ530ileoh8Xvfve7PPjgg8yZM4cLLriA22677RV1XH755Zx//vnceOONPP7441x88cVb56rVatx9991ccsklnHnmmWzcuHHr8scee4zu7m6eeeYZPvvZzzJnzhzmz5//ihq2zL9lzJ133sm73/1uAC666CLmzZvH5MmT6e3t3em+S5Kk4dfsNXELgYUDFs/st75rG2NmNF4/1czc2zJxzEQA7jntnp0ad/PNN7N8+XLGjBkDwFVXXcXxxx/PO9/5Tj74wQ9y2mmnsWTJEgA+85nP8J73vIfe3l4uu+wyvv71r2/dz0033cS4ceN4+umnAXj00Ue54oorGDt27NZ9L1iwgCOOOAKABx98kNNPP33r+FNOOYUrrriCY489FoCf/vSndHd3c99993HSSSex22670dfXx0svvcQPfvAD9t57b3p7e7c+KXrp0qU8//zzvPnNb+Y3v/kNL774Io8++ijd3d2sWrWKc845B2Dr+C2nSX/729/yne98hyeffHKn+iZJklpnRD0nbvWTq5l80GQmHTRpp8adddZZLF68mPHjx/PQQw/R29vLqFGjth6VykwigojY+oiTdevWMX78+Ffs5/zzz6e7u3trqDrqqKP4whe+wM9//vOtN068+OKLzJkzh+7ubq677rpXjD/mmGO46667+MUvfgHAe9/7Xrq7u/nQhz4EwKJFi7j22mvp7Ozkueee49RTT2Xp0qV89atfBaCvr49p06bR3d3N0qVL2WOPPTjqqKPo7u5m+vTpW+dZtGgRM2duzdpMmTKFE088kVWr+t93IkmSXstGVIhb37uec//LuTs9bvHixcyePZtHHnmEI444gnnz5rFo0SImTpzIsmXLmDVrFjNnzmTmzJmcf/753H333fzyl7/kqquu4ic/+Qk/+9nPtrnf1atXc9lllzF69OitN05ceumlzJ49m4suuoivfOUrW7fduHEjc+fO5ayzzuLII4/c5v62hMLvf//7ABx88MEsXLiQWbNmAXD66adzxx13MG/ePObMmbPdv29fXx+TJ08G6kflHn30Ub72ta9xzDHH7HTvJElqV33Zx+KVi4krgw2bNgz7/FHFw3N3la6urtzy3alr165t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\n"
          },
          "metadata": {
            "needs_background": "light"
          }
        },
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "фаренгейт[0]= кельвин[255.372]\n",
            "фаренгейт[10]= кельвин[260.928]\n",
            "фаренгейт[20]= кельвин[266.483]\n",
            "фаренгейт[30]= кельвин[272.039]\n",
            "[[227.5941 ]\n",
            " [260.9277 ]\n",
            " [272.0389 ]\n",
            " [266.4833 ]\n",
            " [260.9277 ]\n",
            " [294.2613 ]\n",
            " [303.70582]]\n",
            "фаренгейта [-50] кельвина [227.5941]\n",
            "фаренгейта [10] кельвина [260.9277]\n",
            "фаренгейта [30] кельвина [272.0389]\n",
            "фаренгейта [20] кельвина [266.4833]\n",
            "фаренгейта [10] кельвина [260.9277]\n",
            "фаренгейта [70] кельвина [294.2613]\n",
            "фаренгейта [87] кельвина [303.70582]\n"
          ]
        }
      ]
    },
    {
      "cell_type": "markdown",
      "source": [
        "Задание 2"
      ],
      "metadata": {
        "id": "PGFaxfvclK08"
      }
    },
    {
      "cell_type": "code",
      "source": [],
      "metadata": {
        "id": "ieQfLZi6lN3Y"
      },
      "execution_count": null,
      "outputs": []
    }
  ]
}