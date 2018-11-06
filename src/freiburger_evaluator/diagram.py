import matplotlib.pyplot as plt


def draw_profile(respondent_data):
    scores = []
    scales_labels = []
    scales = range(1, len(respondent_data.scales) + 1)
    new_line_char = '\n'
    minus_new_line = '-\n'
    for s in respondent_data.scales:
        scores.append(s.standard_score)
        scales_labels.append(f'{s.number}. {s.name.replace("-", minus_new_line).replace(" ", new_line_char)}')
    plt.figure(num=1, figsize=(7.0, 7.0))
    plt.ylabel('Баллы')
    plt.title(f'Профиль личности по Фрайбургскому личностному опроснику\n'
              f'{respondent_data.name}, {respondent_data.email}, {respondent_data.start_timestamp}')
    plt.axis([0, 12.5, 0, 9.5])
    plt.axhline(y=3.5, color='lightcoral', linestyle='--')
    plt.axhline(y=6.5, color='lightcoral', linestyle='--')
    plt.fill([0.0, 0.0, 12.5, 12.5], [0.0, 3.5, 3.5, 0.0], color='b', alpha=0.1)
    plt.fill([0.0, 0.0, 12.5, 12.5], [3.5, 6.5, 6.5, 3.5], color='y', alpha=0.1)
    plt.fill([0.0, 0.0, 12.5, 12.5], [6.5, 9.5, 9.5, 6.5], color='r', alpha=0.1)
    plt.text(0.2, 0.15, "Низкие", style='italic', alpha=0.5)
    plt.text(0.2, 3.65, "Средние", style='italic', alpha=0.5)
    plt.text(0.2, 6.65, "Высокие", style='italic', alpha=0.5)
    plt.xticks(scales, scales_labels)
    plt.tick_params(axis='x', labelrotation=90.0)
    plt.yticks(range(1, 10))
    plt.plot(scales, scores, 'o-')
    plt.grid(True)
    plt.tight_layout()
    plt.show()
