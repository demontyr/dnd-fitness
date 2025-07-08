import project as project
import io
import sys
from unittest.mock import patch
import pytest

def test_calculate_strength():
    print("\nTesting Strength Calculation:")
    project.calculate_strength(bench_pr=90, pushups=15, long_jump=10)
    assert project.strength_score == 10, f"Expected 10, got {project.strength_score}"

def test_calculate_dexterity():
    print("\nTesting Dexterity Calculation:")
    project.calculate_dexterity(balance=5, mile=9.0, burpee=30)
    assert project.dexterity_score == 10, f"Expected 10, got {project.dexterity_score}"

def test_calculate_constitution():
    print("\nTesting Constitution Calculation:")
    project.calculate_constitution(plank=60, breath=90, squats=24)
    assert project.constitution_score == 10, f"Expected 10, got {project.constitution_score}"

def test_calculate_intelligence():
    print("\nTesting Intelligence Calculation:")
    project.calculate_intelligence(edu=2, gpa=2.5)
    assert project.intelligence_score == 10, f"Expected 10, got {project.intelligence_score}"

def test_calculate_wisdom():
    print("\nTesting Wisdom Calculation:")
    project.calculate_wisdom(sleep=75, heart=75, outside=180)
    assert project.wisdom_score == 10, f"Expected 10, got {project.wisdom_score}"

def test_calculate_charisma():
    print("\nTesting Charisma Calculation:")
    project.calculate_charisma(outings=4, interactions=2, dates=1)

    assert project.charisma_score == 10, f"Expected 10, got {project.charisma_score}"

def test_main():
    print("="*50)
    print("STARTING AUTOMATED TESTS")
    print("="*50)
    
    
    print("\nPHASE 1: TESTING INITIAL STAT CALCULATIONS")
    print("-"*50)
    test_calculate_strength()
    test_calculate_dexterity()
    test_calculate_constitution()
    test_calculate_intelligence()
    test_calculate_wisdom()
    test_calculate_charisma()
    
    print("\n All initial stat calculations completed successfully!")
    
    
    print("\nPHASE 2: TESTING MENU OPERATIONS")
    print("-"*50)
    print("Testing sequence:")
    print("1. Display character sheet")
    print("2. Modify strength stat (225 bench, 100 pushups, 10 long jump)")
    print("3. Export character sheet")
    
    test_menu_inputs = [
    "2",     # Display character sheet
    "3",     # Modify stats
    "1",     # Choose strength option
    "225",   # New bench
    "100",   # New pushups
    "10",    # New long jump
    "7", #return to menu
    "4",     # Export
    "6",     # Exit
]
    
    with patch('builtins.input', side_effect=test_menu_inputs):
        captured_output = io.StringIO()
        sys.stdout = captured_output
        
        try:
            project.main()
        except StopIteration:
            pass
        finally:
            sys.stdout = sys.__stdout__
            
        output = captured_output.getvalue()
        print("\nMenu Operations Output:")
        print("-"*50)
        print(output)

    print("="*50)
    print("ALL TESTS COMPLETED SUCCESSFULLY!")
    print("="*50)

if __name__ == "__main__":
    run_all_tests()
    
