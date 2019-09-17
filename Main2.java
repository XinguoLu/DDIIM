//package demo.gene;

import java.io.BufferedReader;
import java.io.BufferedWriter;
import java.io.FileInputStream;
import java.io.FileNotFoundException;
import java.io.FileOutputStream;
import java.io.InputStreamReader;
import java.io.OutputStreamWriter;

public class Main2 {

	public static void main(String[] args) throws Exception{
		new Main2().deal2("F:/test/ganesh", "w");
	}
	public  void deal(String dir,String cancer) throws Exception {
		String datafile1=dir+"/"+cancer+"/"+cancer+"_result.txt";
		String datafile2=dir+"/"+cancer+"/"+cancer+"_cluster_one.txt";
		System.out.println(datafile1+"\n"+datafile2);
		BufferedReader data=new BufferedReader(new InputStreamReader(
				new FileInputStream(datafile1)));

		BufferedWriter data1=new BufferedWriter(new OutputStreamWriter(
				new FileOutputStream(datafile2)));

		String str = data.readLine().trim();
		int k=0;
		while(!str.equals("END")){
			String[] s=str.split("	");

			for(int i=0;i<s.length;i++){
				data1.write(s[i]+"	"+k+"\r\n");
				data1.flush();
			}
			k++;
			String str1=data.readLine();
			if(str1=="" || str1==null)
				break;
			else {
				str=str1.trim();
			}
		}
		data.close();
		data1.close();

	}
	public  void deal2(String dir,String cancer) throws Exception {
		String datafile1=dir+"/"+cancer+"/"+cancer+"1_cluster_one.txt";
		String datafile2=dir+"/"+cancer+"/"+cancer+"1_cluster_result.txt";
		System.out.println(datafile1+"\n"+datafile2);
		BufferedReader data=new BufferedReader(new InputStreamReader(
				new FileInputStream(datafile1)));

		BufferedWriter data1=new BufferedWriter(new OutputStreamWriter(
				new FileOutputStream(datafile2)));

		String str = data.readLine().trim();
		int k=0;
		while(!str.equals("END")){
			String[] s=str.split("	");

			for(int i=0;i<s.length;i++){
				data1.write(s[i]+"	"+k+"\r\n");
				data1.flush();
			}
			k++;
			String str1=data.readLine();
			if(str1=="" || str1==null)
				break;
			else {
				str=str1.trim();
			}
		}
		data.close();
		data1.close();

	}
}
