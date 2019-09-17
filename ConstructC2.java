import java.io.BufferedReader;
import java.io.BufferedWriter;
import java.io.File;
import java.io.FileReader;
import java.io.FileWriter;
import java.util.Arrays;

public class ConstructC2 {
	public static void main(String[] args) throws Exception {
		File file = new File("F:/test/ganesh/GBM/cluster1");
		BufferedReader br = new BufferedReader(new FileReader(file));
		// read data
		String[] geneNames = new String[0];
		int[] modules = new int[0];
		String str = "";
		String[] items = null;
		while(true){
			str = br.readLine();
			if (str == null) 
				break;
			items = str.split("\t");
			geneNames = Arrays.copyOf(geneNames, geneNames.length+1);
			geneNames[geneNames.length-1] = items[0];
			modules = Arrays.copyOf(modules, modules.length+1);
			modules[modules.length-1] = Integer.parseInt(items[1]);
		}
		
		// process
		int max = 0;
		for (int i = 0; i < modules.length; i++) {
			if (max < modules[i]) {
				max = modules[i];
			}
		}
		int[][] array = new int[geneNames.length][max+1];
		
		for (int i = 0; i < modules.length; i++) {
			array[i][modules[i]] = 1;
		}
		//System.out.println(array[0].length);
		
		// write
		File fileOutput = new File("F:/test/ganesh/GBM/cluster1.output.txt");
		BufferedWriter bw = new BufferedWriter(new FileWriter(fileOutput));
		//System.out.println(array.length);
		bw.write("geneID"+"\t");
		for(int n=0;n<array[0].length;n++) {
			bw.write("m"+n+"\t");
		}
		bw.write("\n");//输出第一行的模块号
		for (int i = 0; i < array.length; i++) {
			bw.write(geneNames[i]+"\t");
			for (int j = 0; j < array[0].length; j++) {			
				bw.write(array[i][j] + "\t");
			}
			bw.write("\n");
		}
		bw.flush();
		bw.close();

		
	}
}