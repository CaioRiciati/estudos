import java.util.Scanner;

public class A15ExercicioBreak {
    //dado o valor de um carro, descubra em quantas vezes ele pode ser parcelado
    //condição valorParcela >= 1000
    public static void main(String[] args) {
    double valorCaroo = 4000;

        for(int parcela = 1; parcela <= valorCaroo; parcela++){
            double valorParcela = valorCaroo / parcela;
            if (valorParcela >= 1000) {
            }
            System.out.println("parcela "+ parcela+ " R$ "+valorParcela );

        }

        
    }
}
