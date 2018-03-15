clf, clc

subplot(1,2,1)
plot(RESULT_number_of_words_learnt,'color','blue')
hold on
plot(RESULT_number_of_perception_nodes,'color','red')
title('\textbf{Words learnt}','interpreter','latex')
legend({'Actual words','All nodes'},'location','northwest','interpreter','latex')
xlabel('\textit{time}','interpreter','latex')
ylabel('\textit{number of words}','interpreter','latex')

subplot(2,2,2)
bar(RESULT_word_occurenses)
title('\textbf{Word occurence distribution}','interpreter','latex')
xlabel('\textit{word index}','interpreter','latex')
ylabel('\textit{number of occurences}','interpreter','latex')

subplot(2,2,4)
histogram(RESULT_word_lengths)
title('\textbf{Word length distribution}','interpreter','latex')
xlabel('\textit{word length}','interpreter','latex')
ylabel('\textit{number of occurences}','interpreter','latex')
