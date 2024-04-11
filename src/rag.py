import numpy as np

class SimpleRAG:

    def __init__(self, texts, embeddings) -> None:
        
        self.texts = texts
        self.embeddings = embeddings

    @staticmethod
    def cosine_similarity(vec1, vec2):
        assert len(vec1) == len(vec2), f"Vectors must be of same length, current length: {len(vec1)}, {len(vec2)}"
        dot_product = np.dot(vec1, vec2)
        vec1len = sum(i*i for i in vec1)**0.5
        vec2len = sum(i*i for i in vec2)**0.5

        return dot_product/(vec1len * vec2len)

    def sortSimilarities(self, arr):
        if len(arr) == 0 or len(arr) == 1:
            return arr

        pivot = arr[-1]        
        left = []
        right = []

        for num in arr[:-1]:
            if num > pivot:
                right.append(num)
            else:
                left.append(num)
        return self.sortSimilarities(left) + [pivot] + self.sortSimilarities(right)
    

    def selectTopK(self, question_emb, k):
        similarities = [self.cosine_similarity(question_emb, embedding) for embedding in self.embeddings]
        most_similar = {}

        for index, similarity in enumerate(similarities):
          
            if similarity > 0.55:
                print('adding context')
                most_similar[round(similarity, 5)] = index
        
        arr = [key for key in most_similar]
        sorted_arr = self.sortSimilarities(arr)[-k:]
        indexes = [most_similar[sim] for sim in sorted_arr]
        texts = [self.texts[index] for index in indexes]
        return texts
    

    
