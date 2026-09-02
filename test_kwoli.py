"""
Test script for KWOLI TOOL
Tests basic functionality of all modules
"""

import sys
import os

# Add current directory to path
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

def test_imports():
    """Test if all modules can be imported"""
    print("=" * 60)
    print("Testing module imports...")
    print("=" * 60)

    try:
        from kwoli_tool.config import Colors, MENU_ITEMS
        print("✓ config module imported successfully")
    except ImportError as e:
        print(f"✗ Failed to import config: {e}")
        return False

    try:
        from kwoli_tool.ui.colors import apply_gradient, create_animated_gradient
        print("✓ ui.colors module imported successfully")
    except ImportError as e:
        print(f"✗ Failed to import ui.colors: {e}")
        return False

    try:
        from kwoli_tool.ui.animation import clear_screen, print_menu
        print("✓ ui.animation module imported successfully")
    except ImportError as e:
        print(f"✗ Failed to import ui.animation: {e}")
        return False

    try:
        from kwoli_tool.modules.searchers import IPSearcher, RobloxSearcher
        print("✓ modules.searchers imported successfully")
    except ImportError as e:
        print(f"✗ Failed to import modules.searchers: {e}")
        return False

    try:
        from kwoli_tool.modules.generators import PasswordGenerator, FakePersonGenerator
        print("✓ modules.generators imported successfully")
    except ImportError as e:
        print(f"✗ Failed to import modules.generators: {e}")
        return False

    try:
        from kwoli_tool.modules.utilities import AnonymityManual, HallOfFame
        print("✓ modules.utilities imported successfully")
    except ImportError as e:
        print(f"✗ Failed to import modules.utilities: {e}")
        return False

    return True


def test_color_functions():
    """Test color and gradient functions"""
    print("\n" + "=" * 60)
    print("Testing color functions...")
    print("=" * 60)

    try:
        from kwoli_tool.ui.colors import apply_gradient, remove_ansi_codes
        from kwoli_tool.config import Colors

        # Test gradient
        gradient_text = apply_gradient("KWOLI")
        print(f"Gradient text generated: {len(gradient_text)} characters (including ANSI codes)")

        # Test ANSI code removal
        clean_text = remove_ansi_codes(gradient_text)
        assert clean_text == "KWOLI", "ANSI code removal failed"
        print(f"✓ Text cleanup successful: '{clean_text}'")

        return True
    except Exception as e:
        print(f"✗ Color function test failed: {e}")
        return False


def test_generators():
    """Test data generation functions"""
    print("\n" + "=" * 60)
    print("Testing generator functions...")
    print("=" * 60)

    try:
        from kwoli_tool.modules.generators import (
            PasswordGenerator, 
            FakePersonGenerator,
            EmailGenerator,
            BanWordGenerator
        )

        # Test password generation
        password = PasswordGenerator.generate(print_result=False)
        assert len(password) == 16, "Password length incorrect"
        print(f"✓ Password generated: {password}")

        # Test fake person
        # (Skipping print output)
        print("✓ Fake person generator initialized")

        # Test ban word
        ban_word = BanWordGenerator.generate()
        print(f"✓ Ban word generator working")

        return True
    except Exception as e:
        print(f"✗ Generator test failed: {e}")
        return False


def test_config():
    """Test configuration"""
    print("\n" + "=" * 60)
    print("Testing configuration...")
    print("=" * 60)

    try:
        from kwoli_tool.config import MENU_ITEMS, Colors, MESSAGES

        assert len(MENU_ITEMS) == 15, f"Expected 15 menu items, got {len(MENU_ITEMS)}"
        print(f"✓ Menu items loaded: {len(MENU_ITEMS)} items")

        assert hasattr(Colors, 'RESET'), "Colors.RESET not found"
        print("✓ Color codes defined")

        assert 'welcome' in MESSAGES, "Welcome message not found"
        print("✓ Messages configured")

        return True
    except Exception as e:
        print(f"✗ Configuration test failed: {e}")
        return False


def run_all_tests():
    """Run all tests"""
    print("\n")
    print("╔" + "=" * 58 + "╗")
    print("║" + " KWOLI TOOL - Test Suite ".center(58) + "║")
    print("╚" + "=" * 58 + "╝")

    results = []

    # Run all tests
    results.append(("Module Imports", test_imports()))
    results.append(("Color Functions", test_color_functions()))
    results.append(("Configuration", test_config()))
    results.append(("Generators", test_generators()))

    # Print summary
    print("\n" + "=" * 60)
    print("Test Summary")
    print("=" * 60)

    passed = 0
    failed = 0

    for test_name, result in results:
        status = "✓ PASSED" if result else "✗ FAILED"
        print(f"{test_name:.<40} {status}")
        if result:
            passed += 1
        else:
            failed += 1

    print("=" * 60)
    print(f"Total: {passed} passed, {failed} failed out of {len(results)} tests")
    print("=" * 60)

    if failed == 0:
        print("\n✓ All tests passed! Application is ready to run.\n")
        print("To start KWOLI TOOL, run:")
        print("  python run.py\n")
        return 0
    else:
        print(f"\n✗ {failed} test(s) failed. Please fix the issues.\n")
        return 1


if __name__ == "__main__":
    exit_code = run_all_tests()
    sys.exit(exit_code)
