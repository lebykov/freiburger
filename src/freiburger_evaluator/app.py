import sys
from freiburger_evaluator import evaluator, utils, diagram, loader, reporter


def print_all_summaries(inventory_name, respondents):
    for r in respondents:
        # print(r.compose_summary())
        print(reporter.Reporter.factory(inventory_name, r).compose_summary())
        print('\n\n')


def main(inventory_name, answers_file, scales_file):
    # Refactoring

    # loaded_scales = utils.load_scales(scales_file)
    # print(f'Загрузил таблицу с {len(loaded_scales)} шкалами')
    # loaded_respondents = utils.load_respondents(answers_file, loaded_scales)

    the_loader = loader.Loader.factory(inventory_name, answers_file, scales_file)
    loaded_respondents = the_loader.load_respondents()

    # end Refactoring

    print(f'Уф-ф-ф, загрузил {len(loaded_respondents)} опросников')
    # Refactoring

    for r in loaded_respondents:
        # e = evaluator.Evaluator(r)
        # e.evaluate_raw_scores()
        # e.evaluate_standard_scores()
        e = evaluator.Evaluator.factory(inventory_name, r)
        e.evaluate_respondent()

    # end Refactoring

    print('>>> Чтобы вывести баллы введите номер нужного опросника и нажмите Enter')
    print('>>> Чтобы вывести быллы всех опросников введите 0 и нажмите Enter')
    print('>>> Для выхода введите q')
    print('Опросники')
    for n, r in enumerate(loaded_respondents):
        print(f'{n}. {r.name} {r.email} {r.start_timestamp}')
    print('\n')

    user_input = input("Введите номер опросника или q для выхода: ")
    while user_input != 'q':
        if not user_input.isdigit():
            print(f"Вы ввели \"{user_input}\" вместо номера, попробуйте еще раз =)")
            user_input = input("Введите номер опросника или q для выхода: ")
            continue
        num = int(user_input)
        if 0 > num or num > len(loaded_respondents) - 1:
            print(f'Вы ввели номер {user_input}. Я могу показать результаты для номеров с 0 по {len(loaded_respondents) - 1}')
            user_input = input("Введите номер опросника или q для выхода: ")
            continue
        if num == 0:
            print_all_summaries(inventory_name, loaded_respondents)
        else:
            r = loaded_respondents[num]
            # Refactoring
            # print(r.compose_summary())
            # diagram.draw_profile(r)

            print(reporter.Reporter.factory(inventory_name, r).compose_summary())
            diagram.draw_profile(r)

            # end Refactoring
        user_input = input("Введите номер опросника или q для выхода: ")
    print("До новых встреч, друзья!")


if __name__ == '__main__':
    main(sys.argv[1], sys.argv[2], sys.argv[3])
