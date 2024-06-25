# Create a vector
x <- c(12, 7, 3, 4.2, 18, 2, 54, -21, 8, -5)

# Calculate the mean
result.mean <- mean(x)

# Print the mean
print(result.mean)

# Calculate de median
median.result <- median(x)
print(median.result)

# --------

# Cria um vetor
y <- c(12, 2, 2, 4.2, 18, 2, 54, -21, 8, -5)

# Define uma função para calcular a moda
calculate_mode <- function(v) {
    # Cria uma tabela de frequência dos elementos do vetor
    freq_table <- table(v)

    # Identifica o(s) valor(es) com a maior frequência
    mode_value <- as.numeric(names(freq_table)[freq_table == max(freq_table)])

    # Retorna o(s) valor(es) da moda
    return(mode_value)
}

# Calcula a moda do vetor
result.mode <- calculate_mode(y)

# Imprime a moda
print(result.mode)
