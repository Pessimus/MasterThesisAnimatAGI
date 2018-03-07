%The tests to run
tests_to_run = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100, 110, 120, 130, 140, 150, 160, 170, 180, 190, 200, 210, 220, 230, 240, 250, 260, 270, 280, 290, 300]
%Percentage of times that all generators were found for the different tests:
results_all_generators_found = [0.0, 0.0, 0.0, 0.0, 0.02, 0.05, 0.13, 0.28, 0.41, 0.53, 0.76, 0.77, 0.83, 0.88, 0.92, 0.95, 0.97, 0.98, 0.99, 0.95, 0.99, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0]
% Average percentage of generators found for the different tests:
results_avg_number_of_generators_found = [0.3, 0.52, 0.68, 0.79, 0.85, 0.9, 0.94, 0.96, 0.97, 0.98, 0.99, 0.99, 0.99, 0.99, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0]
plot(tests_to_run,results_all_generators_found)
figure
plot(tests_to_run,results_avg_number_of_generators_found)
