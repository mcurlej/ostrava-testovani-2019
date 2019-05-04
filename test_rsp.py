import subprocess
import sys

import pytest

import rsp
import rsp_lib



def test_rock_is_valid_input():
    result = rsp_lib.is_valid_choice("rock")
    assert result


def test_paper_is_valid_input():
    result = rsp_lib.is_valid_choice("paper")
    assert result


def test_scissors_is_valid_input():
    result = rsp_lib.is_valid_choice("scissors")
    assert result

def test_spock_is_not_valid_input():
    result = rsp_lib.is_valid_choice("spock")
    assert not result

def test_lizard_is_not_valid_input():
    result = rsp_lib.is_valid_choice("lizard")
    assert not result

def test_random_play():
    choices = [rsp_lib.random_choice() for i in range(100)]

    choices = []
    for choice in range(100):
        choices.append(rsp_lib.random_choice())


    assert choices.count('rock') > 10
    assert choices.count('scissors') > 10
    assert choices.count('paper') > 10

    for choice in choices:
       assert rsp_lib.is_valid_choice(choice)


@pytest.mark.parametrize("human,computer", [("rock", "scissors"),
                                            ("scissors", "paper"),
                                            ("paper", "rock")])
def test_get_game_results_when_human_wins(human, computer):
    assert rsp_lib.get_game_results(human, computer) == 1


@pytest.mark.parametrize("human,computer", [("rock", "rock"),
                                            ("scissors", "scissors"),
                                            ("paper", "paper")])
def test_get_game_results_when_tie(human, computer):
    assert rsp_lib.get_game_results(human, computer) == 0


@pytest.mark.parametrize("human,computer", [("scissors", "rock"),
                                            ("paper", "scissors"),
                                            ("rock", "paper")])
def test_get_game_results_when_computer_wins(human, computer):
    assert rsp_lib.get_game_results(human, computer) == -1


def test_print(capsys):
    print("Hello world!")

    captured = capsys.readouterr()

    assert "Hello" in captured.out

def fake_input(promt):
    print(promt)
    return "Rock"

def fake_random_choice(choices):
    return "paper"

def test_full_game_printing(capsys, monkeypatch):
    monkeypatch.setattr('builtins.input', fake_input)
    monkeypatch.setattr('random.choice', fake_random_choice)
    rsp.main()

    captured = capsys.readouterr()
    assert "Rock, Paper, Scissors?" in captured.out
    assert "Computer choice:  paper" in captured.out
    assert "Human choice:  rock" in captured.out
    assert "Human lost!" in captured.out

def test_play_game():
    p = subprocess.run([sys.executable, 'rsp.py'],
                       input='asdd\nrock',
                       encoding='utf-8',
                       stdout=subprocess.PIPE)
    assert p.stdout.count("Rock, Paper, Scissors?") == 2