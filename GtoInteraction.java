import java.io.BufferedReader;
import java.io.BufferedWriter;
import java.io.FileInputStream;
import java.io.FileNotFoundException;
import java.io.FileOutputStream;
import java.io.InputStreamReader;
import java.io.OutputStreamWriter;

public class GtoInteraction {

public static void main(String[] args) throws Exception{
		new GtoInteraction().deal("F:/test/ganesh", "COAD");
		new GtoInteraction().deal("F:/test/ganesh", "GBM");
		
		
	}
	
	public void deal(String dir,String cancer) throws Exception{
		@SuppressWarnings("resource")
		//��ȡ�ļ� gene.txt
		BufferedReader data = new BufferedReader(new InputStreamReader(  
				new FileInputStream(dir+"/"+cancer+"/"+"G.txt")));  
		
		//��һ�У�����ǰ���հ׺�β���հ�
		String strbuff=data.readLine().trim();
		
//		System.out.println("strbuff:"+strbuff);
		
		//���ո��и�,�����ַ�������gene��
        String[] gene = strbuff.split("	"); 
       
        //д���ļ�Ϊgene1.txt
        BufferedWriter data1 = new BufferedWriter(new OutputStreamWriter(  
				new FileOutputStream(dir+"/"+cancer+"/"+"G1.txt"))); 
        
        for(int i=0;i<gene.length;i++){
        	String temp=data.readLine().trim();
//        	System.out.println(temp);
        	
        	String[] s2=temp.split("	");
        	
        	for(int j=i+1;j<gene.length;j++){
	        	 data1.write(gene[i]+"	"+gene[j]+"	"+s2[j+1]+"\r\n");
	        	 data1.flush();
        	}
        }
		
		
		
	}

}


