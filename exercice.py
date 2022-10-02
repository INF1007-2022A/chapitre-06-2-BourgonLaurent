#!/usr/bin/env python
# -*- coding: utf-8 -*-

from matplotlib.colors import cnames


def list_to_dict(some_list: list) -> dict:
    return {k: i for i, k in enumerate(some_list)}


def color_name_to_hex(colors: list) -> list:
    return [(c, cnames[c]) for c in colors]


def create_list() -> list:
    return [n for n in range(0, 10_000) if not 15 <= n <= 350]


def compute_mse(model_dict: dict) -> dict:
    # TODO: Calculer l'erreur quadratique moyen pour chaque modèle. Retourner un dictionnaire contenant les MSE.

    return {}


def main() -> None:
    some_list = ["a", "b", "z", "patate"]
    print(
        f"La liste suivante {some_list} est transformée en dictionnaire: {list_to_dict(some_list)}"
    )

    colors = ["blue", "red", "green", "yellow", "black", "white"]
    print(f"La valeur hex associée aux couleurs est: {color_name_to_hex(colors)}")

    print(f"La liste des 10000 entiers est: {create_list()}")

    model_dict = {
        "LR": [(90, 92), (96, 100), (20, 25), (21, -2), (3, -20)],
        "DNN": [(100, 101), (50, 50), (1, 2), (-10, -12), (-1, 7)],
        "RF": [(10, 19), (56, 70), (1, 9), (-100, -12), (-11, 7)],
    }
    print(f"Le mse des différents modèles est: {compute_mse(model_dict)}")


if __name__ == "__main__":
    main()
