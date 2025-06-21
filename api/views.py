from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.parsers import MultiPartParser
import pandas as pd
from sklearn.cluster import KMeans

class AnaliseCSVView(APIView):
    parser_classes = [MultiPartParser]

    def post(self, request, *args, **kwargs):
        if 'file' not in request.FILES:
            return Response({'erro': 'Nenhum arquivo enviado.'}, status=400)

        # Lê o arquivo CSV enviado
        arquivo = request.FILES['file']
        try:
            df = pd.read_csv(arquivo)
        except Exception as e:
            return Response({'erro': f'Erro ao ler o CSV: {str(e)}'}, status=400)

        # Verifica se tem a coluna que a gente espera
        if 'quantidade_passageiros' not in df.columns:
            return Response({'erro': 'Coluna "quantidade_passageiros" não encontrada no CSV.'}, status=400)

        # Aplica KMeans para classificar linhas com base no número de passageiros
        try:
            kmeans = KMeans(n_clusters=3, random_state=0)
            df['cluster'] = kmeans.fit_predict(df[['quantidade_passageiros']])

            # Nomear os clusters como Alta, Média ou Baixa demanda
            media_por_cluster = df.groupby('cluster')['quantidade_passageiros'].mean().sort_values()
            nomes_clusters = {}
            nomes = ['Baixa', 'Média', 'Alta']
            for i, cluster in enumerate(media_por_cluster.index):
                nomes_clusters[cluster] = nomes[i]

            df['classificacao'] = df['cluster'].map(nomes_clusters)

            # Seleciona apenas as colunas relevantes para retornar
            resultado = df[['linha', 'quantidade_passageiros', 'classificacao']].to_dict(orient='records')

            return Response({'resultado': resultado})
        except Exception as e:
            return Response({'erro': f'Erro na análise: {str(e)}'}, status=500)
