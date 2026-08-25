{
  "nbformat": 4,
  "nbformat_minor": 0,
  "metadata": {
    "colab": {
      "provenance": [],
      "authorship_tag": "ABX9TyNKWbUs1Ccf39oanT5vxF3W",
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
        "<a href=\"https://colab.research.google.com/github/Mackan08/Na3a-programmering-riktiga/blob/main/Kalkylator.py\" target=\"_parent\"><img src=\"https://colab.research.google.com/assets/colab-badge.svg\" alt=\"Open In Colab\"/></a>"
      ]
    },
    {
      "cell_type": "code",
      "execution_count": null,
      "metadata": {
        "id": "HrDXX1oS3q7C"
      },
      "outputs": [],
      "source": [
        "print(\"Hej, Vad heter du?\")\n",
        "name = input()\n",
        "print(\"Hej\", name)\n",
        "birthyear = input(\"födelseår: \")\n",
        "aktuellt_år = 2026\n",
        "print (\"Hej,\", name, \"Din ålder är\", aktuellt_år - int(birthyear), \"år\")\n",
        "print (int(3.1))"
      ]
    },
    {
      "cell_type": "markdown",
      "source": [
        "Vad händer om?\n",
        "Efter jag testade skriva in print(int(3.9)) samt även testade (int(3.1)) printade programmet bara ut trean i slutet av chatten- Slutsatsen jag drar är att programet bara printar ut trean som kommer före punkten och inte den som sitter bakom. Varför vet jag faktiskt inte, eventuellt punkten mellan dom.\n",
        "README\n",
        "Eftersom namnet funkar som en string medan födelseåret måste konverteras om till en integer. När jag skrev ord fick jag fram error och programmet kraschade."
      ],
      "metadata": {
        "id": "oNF8RRV-4WS7"
      }
    },
    {
      "cell_type": "code",
      "source": [
        "tal1 = float(input(\"Skriv in ditt första tal: \"))\n",
        "tal2 = float(input(\"Skriv in ditt andra tal: \"))\n",
        "summa = tal1 + tal2\n",
        "differens = tal1 - tal2\n",
        "produkt = tal1 * tal2\n",
        "print(f\"summan av talen är: {summa}\")\n",
        "print(f\"differensen av talen är: {differens}\")\n",
        "print(f\"produkten av talen är: {produkt}\")"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "3mJANtSx6gut",
        "outputId": "06d1d7e4-fd94-4ed6-cc4c-cbf1e2ae0a37"
      },
      "execution_count": 8,
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "Skriv in ditt första tal: 234\n",
            "Skriv in ditt andra tal: 12\n",
            "summan av talen är: 246.0\n",
            "differensen av talen är: 222.0\n",
            "produkten av talen är: 2808.0\n"
          ]
        }
      ]
    }
  ]
}