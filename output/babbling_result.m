%The tests to run
tests_to_run = [10, 20, 30]
%Percentage of times that all generators were found for the different tests:
results_all_generators_found = [0, 0, 0]
% Average percentage of generators found for the different tests:
results_avg_number_of_generators_found = [0.35, 0.5, 0.73]
plot(tests_to_run,results_all_generators_found)
figure
plot(tests_to_run,results_avg_number_of_generators_found)
