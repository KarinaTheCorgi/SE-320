============================= test session starts ==============================
collecting ... collected 11 items

tests/test_bank_account.py::test_to_json PASSED                          [  9%]
tests/test_bank_account.py::test_from_json PASSED                        [ 18%]
tests/test_bank_account.py::test_deposit PASSED                          [ 27%]
tests/test_bank_account.py::test_deposit_negative_amount PASSED          [ 36%]
tests/test_bank_account.py::test_withdraw[100] PASSED                    [ 45%]
tests/test_bank_account.py::test_withdraw_too_much[250] PASSED           [ 54%]
tests/test_bank_account.py::test_withdraw_negative_amount PASSED         [ 63%]
tests/test_bank_account.py::test_get_balance PASSED                      [ 72%]
tests/test_bank_account.py::test_withdraw_zero PASSED                    [ 81%]
tests/test_bank_account.py::test_deposit_zero PASSED                     [ 90%]
tests/test_bank_account.py::test_negative_init PASSED                    [100%]

============================== 11 passed in 0.01s ==============================
