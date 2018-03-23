clf, clc

yyaxis left
plot(tests_to_run,results_all_generators_found*100)
ylabel('Percentage of runs where all generators were found','interpreter','latex')
hold on
yyaxis right
plot(tests_to_run,results_avg_number_of_generators_found*100)
ylabel('Average percentage of generators found per run','interpreter','latex');
title('\textbf{Statistics of how well the Animat finds generators}','interpreter','latex');
xlabel('Number of timesteps spent babbling','interpreter','latex');
